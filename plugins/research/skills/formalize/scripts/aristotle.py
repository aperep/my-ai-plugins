# /// script
# requires-python = ">=3.12"
# dependencies = ["aristotlelib==2.1.0"]
# ///
"""Small, resumable Aristotle client. Remote results stay generated until reviewed."""
import argparse
import asyncio
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import tarfile


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def save(run, data):
    pending = run / "request.json.tmp"
    pending.write_text(json.dumps(data, indent=2) + "\n")
    pending.replace(run / "request.json")


def prepare(project, run, prompt, files):
    project = project.resolve()
    selected = {}
    for name in files:
        relative = Path(name)
        path = project / relative
        if (relative.is_absolute() or ".." in relative.parts
                or any(part.startswith(".") for part in relative.parts)
                or path.resolve() != path or not path.is_file()):
            raise ValueError(f"Expected an explicit regular project file: {name}")
        selected[relative.as_posix()] = path
    if not selected:
        raise ValueError("Select at least one input file")
    run.mkdir(parents=True, exist_ok=False)
    with tarfile.open(run / "input.tar.gz", "w:gz") as archive:
        for name, path in selected.items():
            archive.add(path, arcname=name)
    data = {
        "sdk": "aristotlelib==2.1.0", "prompt": prompt,
        "files": {name: digest(path) for name, path in selected.items()},
        "input_sha256": digest(run / "input.tar.gz"),
        "submission": "prepared", "project_id": None,
        "formal_status": "generated",
    }
    # 'generated' describes the Lean request, never proof acceptance.
    save(run, data)
    return data


def validate_snapshot(run, data):
    if digest(run / "input.tar.gz") != data["input_sha256"]:
        raise ValueError("Input archive changed; prepare a new attempt")


def extract_result(archive, destination):
    with tarfile.open(archive) as bundle:
        for member in bundle.getmembers():
            path = PurePosixPath(member.name)
            if (path.is_absolute() or ".." in path.parts
                    or not (member.isfile() or member.isdir())):
                raise ValueError(f"Unsafe result archive member: {member.name}")
        destination.mkdir(parents=True, exist_ok=False)
        bundle.extractall(destination, filter="data")


async def remote(action, run):
    if not os.environ.get("ARISTOTLE_API_KEY"):
        raise ValueError("Set ARISTOTLE_API_KEY in the environment; do not pass it as an argument")
    from aristotlelib.project import Project, ProjectStatus
    from aristotlelib.api_request import AristotleRequestClient

    data = json.loads((run / "request.json").read_text())
    if action == "submit":
        validate_snapshot(run, data)
        if data["submission"] != "prepared":
            raise ValueError("Attempt already submitted or outcome uncertain; inspect Aristotle history before retrying")
        # Persist intent BEFORE the remote write: a timeout must not silently resubmit.
        data["submission"] = "uncertain"
        save(run, data)
        project = await Project.create(
            prompt=data["prompt"], tar_file_path=run / "input.tar.gz",
            public_file_path="input.tar.gz",
        )
        data.update(project_id=project.project_id, submission="submitted")
        save(run, data)
        return data

    if not data["project_id"]:
        raise ValueError("No recorded project ID; submit first or recover it from Aristotle history")
    project = await Project.from_id(data["project_id"])
    tasks, _ = await project.get_tasks(limit=1)
    data["remote_project_status"] = project.status.name
    data["latest_task"] = tasks[0].model_dump(mode="json") if tasks else None
    save(run, data)
    if action == "fetch":
        if project.status != ProjectStatus.IDLE or not project.has_files:
            raise ValueError("No idle project result yet; use status later")
        archive = run / "result.tar.gz"
        if archive.exists() or (run / "result").exists():
            raise FileExistsError("Result already exists; preserve it before downloading a newer revision")
        # get_files() may fall back to the INPUT archive. Request only the result.
        async with AristotleRequestClient() as client:
            response = await client.get(f"/project/{project.project_id}/result")
        with archive.open("xb") as output:
            output.write(response.content)
        data["result_sha256"] = digest(archive)
        data["formal_status"] = "generated"
        save(run, data)
        extract_result(archive, run / "result")
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare_parser = commands.add_parser("prepare", help="Snapshot only explicitly named files; no network")
    prepare_parser.add_argument("--project", type=Path, required=True)
    prepare_parser.add_argument("--run", type=Path, required=True)
    prepare_parser.add_argument("--prompt-file", type=Path, required=True)
    prepare_parser.add_argument("--file", action="append", required=True)
    for command in ["submit", "status", "fetch"]:
        child = commands.add_parser(command)
        child.add_argument("run", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            data = prepare(args.project, args.run, args.prompt_file.read_text(), args.file)
        else:
            data = asyncio.run(remote(args.command, args.run))
        print(json.dumps(data, indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
