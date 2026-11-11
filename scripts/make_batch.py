#!/usr/bin/env python3
"""Compile a batch of tailored CVs and cover letters and zip the PDFs.

Expected layout:

    batches/2026-11-02/
        01_CompanyA/cv.tex, cover_letter.tex
        02_CompanyB/cv.tex, cover_letter.tex

Usage:

    python scripts/make_batch.py batches/2026-11-02 --name "Firstname_Lastname"

Output: batches/2026-11-02.zip containing PDFs only, in the same numbered
folders, named <name>_CV.pdf and <name>_Cover_Letter.pdf.
"""
import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path

DOCS = {"cv.tex": "CV", "cover_letter.tex": "Cover_Letter"}


def compile_tex(tex: Path) -> Path:
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
        cwd=tex.parent, capture_output=True, text=True, errors="replace",
    )
    pdf = tex.with_suffix(".pdf")
    if result.returncode != 0 or not pdf.exists():
        tail = "\n".join(result.stdout.splitlines()[-15:])
        raise RuntimeError(f"pdflatex failed for {tex}:\n{tail}")
    return pdf


def page_count(tex: Path) -> int:
    log = tex.with_suffix(".log").read_text(errors="replace")
    match = re.search(r"Output written on .*?\((\d+) pages?", log, re.S)
    return int(match.group(1)) if match else -1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("batch_dir", type=Path)
    parser.add_argument("--name", required=True, help='e.g. "Firstname_Lastname"')
    args = parser.parse_args()

    folders = sorted(p for p in args.batch_dir.iterdir() if p.is_dir())
    if not folders:
        print(f"No posting folders in {args.batch_dir}")
        return 1

    problems, entries = [], []
    numbers = []
    for folder in folders:
        match = re.match(r"(\d+)_", folder.name)
        if not match:
            problems.append(f"{folder.name}: folder name must start with a number, e.g. 01_Company")
            continue
        numbers.append(int(match.group(1)))
        for tex_name, label in DOCS.items():
            tex = folder / tex_name
            if not tex.exists():
                problems.append(f"{folder.name}: missing {tex_name}")
                continue
            try:
                pdf = compile_tex(tex)
            except RuntimeError as err:
                problems.append(str(err))
                continue
            pages = page_count(tex)
            if pages != 1:
                problems.append(f"{folder.name}/{tex_name}: {pages} pages (must be 1)")
            entries.append((pdf, f"{folder.name}/{args.name}_{label}.pdf"))

    expected = list(range(1, len(numbers) + 1))
    if sorted(numbers) != expected:
        problems.append(f"Folder numbers {sorted(numbers)} are not a clean 1..{len(numbers)} sequence")

    if problems:
        print("Not zipping. Fix these first:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    zip_path = args.batch_dir.parent / f"{args.batch_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for pdf, arcname in entries:
            archive.write(pdf, arcname)

    print(f"Wrote {zip_path}")
    for _, arcname in entries:
        print(f"  {arcname}")
    print("Check that each folder number matches the same number on your list before sending.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
