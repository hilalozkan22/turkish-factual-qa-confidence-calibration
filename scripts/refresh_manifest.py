#!/usr/bin/env python3
"""Regenerate SHA-256 release manifest after *final* repository edits (stdlib only).

Run: python scripts/refresh_manifest.py
Then: python scripts/verify_release.py
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "release_manifest.json"
DIRECTORIES = ("configs", "data", "docs", "notebooks", "prompts", "scripts")
TOP_FILES = ("README.md", "CITATION.cff", "LICENSE")

def public_files():
    """Enumerate files expected in the public release; omit local/hidden artifacts."""
    paths = [ROOT / name for name in TOP_FILES if (ROOT / name).is_file()]
    for name in DIRECTORIES:
        folder = ROOT / name
        if folder.is_dir():
            paths.extend(p for p in folder.rglob("*") if p.is_file())
    return sorted((p for p in paths
                   if p != MANIFEST
                   and not any(x.startswith(".") or x == "__pycache__" for x in p.relative_to(ROOT).parts)
                   and p.suffix not in {".pyc", ".zip"}),
                  key=lambda p: p.relative_to(ROOT).as_posix())

def compute_checksums():
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in public_files()}

if __name__ == "__main__":
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["output_sha256"] = compute_checksums()
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"UPDATED {MANIFEST.relative_to(ROOT)}: {len(manifest['output_sha256'])} files")
