#!/usr/bin/env python3
"""Assemble Quarto book chapters into a single WECA-branded Typst PDF.

Strips YAML front matter from each chapter, injects the title as a
level-1 heading, then renders the combined document with the
weca-report-typst format.  The generated training-report.qmd is
intentionally excluded from git (see .gitignore).

Usage:
    uv run scripts/build_typst_report.py
"""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Chapters in book order (mirrors _quarto.yml)
CHAPTERS = [
    "index.qmd",
    "overview/course-plan.qmd",
    "overview/pedagogy.qmd",
    "sessions/session-01.qmd",
    "sessions/session-02.qmd",
    "sessions/session-03.qmd",
    "sessions/session-04.qmd",
    "sessions/session-05.qmd",
    "resources/datasets.qmd",
    "resources/setup-guide.qmd",
    "resources/troubleshooting.qmd",
]

FRONT_MATTER = """\
---
title: "WECA R & Quarto Training"
subtitle: "From Excel to Code-First Analysis"
author: "WECA Analysis Team"
date: last-modified
format:
  weca-report-typst:
    toc: true
    toc-depth: 3
    section-numbering: "1.1"
execute:
  eval: false
  echo: true
  error: true
  warning: false
  message: false
knitr:
  opts_chunk:
    message: false
    warning: false
    comment: "#>"
    fig.align: "center"
---

"""

_YAML_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Match `r expr` but not ``...`` double-backtick escapes
_INLINE_R_RE = re.compile(r"(?<!`)`r\s+([^`]+)`(?!`)")


def extract_meta(yaml_text: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for line in yaml_text.splitlines():
        for key in ("title", "subtitle"):
            if line.startswith(f"{key}:"):
                meta[key] = line[len(key) + 1 :].strip().strip("\"'")
    return meta


def process_chapter(path: Path, is_index: bool = False) -> str:
    text = path.read_text(encoding="utf-8")
    m = _YAML_RE.match(text)
    if m:
        meta = extract_meta(m.group(1))
        body = text[m.end() :]
    else:
        meta = {}
        body = text

    heading = ""
    if not is_index:
        if title := meta.get("title"):
            heading = f"# {title}\n\n"
        if subtitle := meta.get("subtitle"):
            heading += f"*{subtitle}*\n\n"

    body = _INLINE_R_RE.sub(r"`\1`", body)
    return heading + body.lstrip("\n")


def build() -> None:
    out = ROOT / "training-report.qmd"

    parts = [FRONT_MATTER]
    for i, rel in enumerate(CHAPTERS):
        chapter_path = ROOT / rel
        parts.append(process_chapter(chapter_path, is_index=(i == 0)))
        parts.append("\n\n")

    out.write_text("".join(parts), encoding="utf-8")
    print(f"Assembled {out.name} ({len(CHAPTERS)} chapters)")

    result = subprocess.run(
        ["quarto", "render", out.name],
        cwd=ROOT,
    )
    if result.returncode != 0:
        raise SystemExit(f"quarto render failed (exit code {result.returncode})")

    print(f"PDF written to {ROOT / 'training-report.pdf'}")


if __name__ == "__main__":
    build()
