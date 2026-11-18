"""news-image-20261118 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a single newspaper
front page summing up the world's news of Wednesday 18 November 2026 in
32 stories. The program copies it, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). No network, no
randomness, no timestamps in the output: two runs produce identical bytes.

The image itself was drawn by build_entry.py (Python + Pillow, run locally):
a dense broadsheet with two BIG painted hero panels at the top (the Kerch
Bridge collapse and the Bahrain firefight, together ~45% of the page),
8 more featured stories with a small flat illustration each, 22 one-line
briefs, a numbered world map and a sources footer. All facts were checked
against live news reporting of 17-18 November 2026; disputed claims are
attributed in the image.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576  # 1 MiB gate limit
MAX_DIMENSION = 1024  # 1024x1024 gate limit
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message: str) -> "SystemExit":
    print(f"error: {message}", file=sys.stderr)
    return SystemExit(1)


def read_png_dimensions(path: str) -> tuple[int, int]:
    """Return (width, height) parsed from the PNG IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file (bad magic bytes)")
    if header[12:16] != b"IHDR":
        raise ValueError("not a PNG file (first chunk is not IHDR)")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

    if not os.path.isfile(source):
        raise SystemExit(fail(f"source image missing: {source}"))

    size = os.path.getsize(source)
    if size > MAX_BYTES:
        raise SystemExit(fail(f"entry.png is {size} bytes, over the 1 MiB limit"))

    width, height = read_png_dimensions(source)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise SystemExit(
            fail(f"entry.png is {width}x{height}, over the 1024x1024 limit")
        )

    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError:
        # Fallback: the requested output dir cannot be created (read-only
        # parent, permissions). Use a local ./out dir next to this file
        # instead of failing the run outright.
        fallback = os.path.join(here, "out")
        print(
            f"warning: cannot create {output_dir}, falling back to {fallback}",
            file=sys.stderr,
        )
        output_dir = fallback
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError as exc:
            raise SystemExit(fail(f"cannot create output dir {output_dir}: {exc}"))
    if not os.path.isdir(output_dir):
        raise SystemExit(fail(f"output path is not a directory: {output_dir}"))

    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)

    # Verify the copy: same size and same PNG magic, so a truncated or
    # partial write is caught here instead of reaching the judge.
    copied_size = os.path.getsize(destination)
    if copied_size != size:
        raise SystemExit(
            fail(f"copy incomplete: {destination} is {copied_size} bytes, "
                 f"expected {size}")
        )
    with open(destination, "rb") as handle:
        if handle.read(8) != PNG_MAGIC:
            raise SystemExit(fail(f"copy failed validation: {destination}"))
    print(f"wrote {destination} ({width}x{height}, {size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
