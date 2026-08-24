#!/usr/bin/env python3
"""Enable conservative auto-evolution inside this marketplace."""

import json
import os
from pathlib import Path


def in_marketplace(start):
    for path in (start, *start.parents):
        if (path / ".agents/plugins/marketplace.json").is_file() and (
            path / "plugins"
        ).is_dir():
            return True
    return False


if in_marketplace(Path(os.getcwd()).resolve()):
    context = (
        "Auto-evolution is enabled for this marketplace. When this task yields a "
        "validated, reusable suggestion about building or maintaining its plugins, "
        "use the evolving-plugins skill before the final response: harvest the "
        "suggestion, map it to an existing skill first, and draft the smallest "
        "reviewable change. Skip one-off or uncertain ideas. Obey content guards; "
        "never stamp your own work."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            }
        )
    )
