"""Reject stale curriculum/export snapshots. Hashes do not replace visual/content review."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    manifest = json.loads((ROOT / "04-enablement/curriculum-export-manifest.json").read_text())
    for relative, expected in manifest["files"].items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(f"Stale curriculum snapshot: {relative}; regenerate and review both downloads")
    pptx = ROOT / "04-enablement/HR-AI-Literacy-Curriculum.pptx"
    with ZipFile(pptx) as archive:
        slides = [p for p in archive.namelist() if p.startswith("ppt/slides/slide") and p.endswith(".xml")]
        if len(slides) != manifest["slides"]:
            raise SystemExit("Curriculum slide count changed")
        source_hash = manifest["files"]["04-enablement/hr-ai-literacy-curriculum.md"]
        notes = [p for p in archive.namelist() if p.startswith("ppt/notesSlides/notesSlide") and p.endswith(".xml")]
        if len(notes) != manifest["slides"] or any(source_hash not in archive.read(p).decode() for p in notes):
            raise SystemExit("PowerPoint notes do not identify the current source snapshot")
    print("Curriculum source and visually reviewed download snapshots match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
