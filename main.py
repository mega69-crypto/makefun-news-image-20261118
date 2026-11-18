#!/usr/bin/env python3
"""Copy the finished entry image to the output directory.

Stdlib only, no network. The image is rendered at build time from
render.html; this program just places it at /output/entry.png.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    size = dest.stat().st_size
    if size > 1_048_576:
        raise SystemExit(f"entry.png too large: {size} bytes (limit 1048576)")
    print(f"wrote {dest} ({size} bytes)")


if __name__ == "__main__":
    main()
