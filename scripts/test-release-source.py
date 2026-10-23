#!/usr/bin/env python3
"""Keep deployment-generated GitHub release content out of website commits."""

import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
tracked = subprocess.run(
    ["git", "-C", str(root), "ls-files", "-z"],
    check=True,
    capture_output=True,
).stdout.decode().split("\0")
generated_pages = [
    path for path in tracked
    if path.startswith("src/pages/releases/")
    and path.lower().endswith((".md", ".mdx"))
]
if generated_pages:
    print("Generated GitHub release pages must not be committed:", file=sys.stderr)
    print("\n".join(generated_pages), file=sys.stderr)
    raise SystemExit(1)

catalog_path = root / "src/data/releases.json"
if "src/data/releases.json" not in tracked or json.loads(catalog_path.read_text()) != []:
    print("src/data/releases.json must remain the empty deployment input.", file=sys.stderr)
    raise SystemExit(1)

print("Generated GitHub release pages remain deployment-only.")
