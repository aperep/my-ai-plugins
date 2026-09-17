"""Offline tests: uv run --with aristotlelib==2.1.0 python -m unittest discover -s scripts."""
import importlib.util
import io
import json
import os
from pathlib import Path
import tarfile
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

spec = importlib.util.spec_from_file_location("runner", Path(__file__).with_name("aristotle.py"))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class PipelineTests(unittest.TestCase):
    def test_snapshot_is_explicit_and_immutable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Target.lean").write_text("theorem target : True := by trivial\n")
            (root / ".env").write_text("SECRET=not-for-upload")
            run = root / "run"
            runner.prepare(root, run, "Prove target", ["Target.lean"])
            data = json.loads((run / "request.json").read_text())
            with tarfile.open(run / "input.tar.gz") as archive:
                self.assertEqual(archive.getnames(), ["Target.lean"])
            (root / "Target.lean").write_text("changed")
            runner.validate_snapshot(run, data)
            with self.assertRaises(FileExistsError):
                runner.prepare(root, run, "again", ["Target.lean"])
            (run / "input.tar.gz").write_bytes(b"changed archive")
            with self.assertRaises(ValueError):
                runner.validate_snapshot(run, data)

    def test_paths_cannot_escape_or_follow_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "linked").symlink_to("/etc/hostname")
            for name in ["../secret", "/etc/hostname", "linked", ".env"]:
                with self.subTest(name=name), self.assertRaises(ValueError):
                    runner.prepare(root, root / "run", "prompt", [name])

    def test_extract_rejects_traversal_and_links(self):
        for name, kind in [("../escape", tarfile.REGTYPE), ("/escape", tarfile.REGTYPE),
                           ("link", tarfile.SYMTYPE)]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                archive = root / "result.tar.gz"
                with tarfile.open(archive, "w:gz") as out:
                    entry = tarfile.TarInfo(name)
                    entry.type = kind
                    entry.linkname = "/etc/hostname"
                    out.addfile(entry, io.BytesIO(b""))
                with self.assertRaises(ValueError):
                    runner.extract_result(archive, root / "result")

    def test_extract_keeps_good_files_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "result.tar.gz"
            with tarfile.open(archive, "w:gz") as out:
                entry = tarfile.TarInfo("Proof.lean")
                entry.size = 4
                out.addfile(entry, io.BytesIO(b"test"))
            runner.extract_result(archive, root / "result")
            self.assertEqual((root / "result/Proof.lean").read_text(), "test")
            with self.assertRaises(FileExistsError):
                runner.extract_result(archive, root / "result")


class RemoteTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "Target.lean").write_text("example : True := by trivial")
        self.run = self.root / "attempt"
        runner.prepare(self.root, self.run, "prove", ["Target.lean"])
        self.env = patch.dict(os.environ, {"ARISTOTLE_API_KEY": "offline-test-placeholder"})
        self.env.start()
        self.addCleanup(self.env.stop)

    async def test_submit_persists_id_and_never_resubmits(self):
        with patch("aristotlelib.project.Project.create", new_callable=AsyncMock) as create:
            create.return_value = SimpleNamespace(project_id="job-1")
            data = await runner.remote("submit", self.run)
            self.assertEqual(data["project_id"], "job-1")
            self.assertEqual(json.loads((self.run / "request.json").read_text())["project_id"], "job-1")
            with self.assertRaises(ValueError):
                await runner.remote("submit", self.run)
            create.assert_awaited_once()

    async def test_timeout_leaves_uncertain_submission(self):
        with patch("aristotlelib.project.Project.create", new_callable=AsyncMock) as create:
            create.side_effect = TimeoutError("simulated response loss")
            with self.assertRaises(TimeoutError):
                await runner.remote("submit", self.run)
            with self.assertRaises(ValueError):
                await runner.remote("submit", self.run)
            create.assert_awaited_once()

    async def test_status_is_one_poll_and_fetch_requires_result(self):
        from aristotlelib.project import ProjectStatus
        data = json.loads((self.run / "request.json").read_text())
        data.update(project_id="job-1", submission="submitted")
        runner.save(self.run, data)
        task = SimpleNamespace(model_dump=lambda **kw: {"status": "COMPLETE"})
        project = SimpleNamespace(status=ProjectStatus.IDLE, has_files=False,
                                  get_tasks=AsyncMock(return_value=([task], None)))
        with patch("aristotlelib.project.Project.from_id", new_callable=AsyncMock) as get:
            get.return_value = project
            data = await runner.remote("status", self.run)
            project.get_tasks.assert_awaited_once()
            self.assertEqual(data["formal_status"], "generated")
            with self.assertRaises(ValueError):
                await runner.remote("fetch", self.run)
            self.assertFalse((self.run / "result.tar.gz").exists())

    async def test_missing_key_keeps_prepared_attempt(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "ARISTOTLE_API_KEY"):
                await runner.remote("submit", self.run)
        self.assertEqual(json.loads((self.run / "request.json").read_text())["submission"], "prepared")

    async def test_fetch_preserves_archive_and_generated_state(self):
        from aristotlelib.project import ProjectStatus
        data = json.loads((self.run / "request.json").read_text())
        data.update(project_id="job-1", submission="submitted")
        runner.save(self.run, data)
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as out:
            entry = tarfile.TarInfo("Proof.lean")
            entry.size = 4
            out.addfile(entry, io.BytesIO(b"test"))
        project = SimpleNamespace(status=ProjectStatus.IDLE, has_files=True,
                                  project_id="job-1", get_tasks=AsyncMock(return_value=([], None)))
        with patch("aristotlelib.project.Project.from_id", new_callable=AsyncMock) as get, \
                patch("aristotlelib.api_request.AristotleRequestClient") as client:
            get.return_value = project
            connection = client.return_value.__aenter__.return_value
            connection.get.return_value = SimpleNamespace(content=buffer.getvalue())
            data = await runner.remote("fetch", self.run)
            connection.get.assert_awaited_once_with("/project/job-1/result")
            self.assertEqual((self.run / "result/Proof.lean").read_text(), "test")
            self.assertEqual(data["formal_status"], "generated")
            self.assertEqual(data["result_sha256"], runner.digest(self.run / "result.tar.gz"))
            with self.assertRaises(FileExistsError):
                await runner.remote("fetch", self.run)


if __name__ == "__main__":
    unittest.main()
