# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Quarto book project containing training materials for a 5-session course teaching WECA analysts to use R, Quarto, and Git. This is **not** a software project - it's a documentation/curriculum site that renders to HTML.

## Build Commands

```bash
# Render the full book
quarto render

# Preview with live reload
quarto preview

# Render a single chapter
quarto render sessions/session-03.qmd
```

No tests, linters, or build pipelines exist for this project.

## Architecture

- **Quarto book** configured in `_quarto.yml` (type: book, output to `_output/`)
- **Freeze mode** (`execute: freeze: auto`) - code chunks are cached in `_freeze/` and only re-executed when source changes
- **SCSS theming** in `custom.scss` using WECA brand colours (`$weca-purple: #4B1E78`, `$weca-claret: #971B2F`, `$weca-forest-green: #006747`, `$weca-light-blue: #009FE3`)
- **Dual format** output: HTML (primary, cosmo theme + custom SCSS) and PDF (report class, A4)

## Content Structure

All content is `.qmd` (Quarto Markdown) files organised as book chapters:

- `index.qmd` - Landing page
- `overview/` - Course design docs (course-plan, pedagogy)
- `sessions/session-01.qmd` through `session-05.qmd` - Lesson plans with embedded R code examples
- `resources/` - Setup guide, datasets reference, troubleshooting

## Key Conventions

- R code examples use **tidyverse** packages, `here::here()` for paths, and WECA helper functions (`theme_weca()`, `get_weca_color()`, `show_weca_palette()`)
- Code examples reference the companion **indicators** project at `../indicators/` - they are teaching materials, not runnable code in this repo
- The `knitr` and `jupyter: python3` engines are both configured, but content is primarily R-focused
- Session files follow a consistent structure: Learning Outcomes, Session Structure (numbered Parts), Wrap-up & Homework
- Branch naming convention taught: `yourname/chapter-or-feature`
- Consecutive `**Bold Label:**` metadata lines (e.g. Duration, Goal, Format) must use `- ` list prefix so each renders on its own line. Without `- `, Markdown collapses them into a single paragraph.

## Showing Verbatim Code in Quarto

Knitr scans the entire `.qmd` file for executable code **before** pandoc processes markdown. Plain code fences (even with more backticks) do NOT prevent execution. Use these patterns:

**Verbatim code chunks** — use double curly braces `{{r}}` in the opening fence, wrapped in a 4-backtick outer fence:

    ````
    ```{{r}}
    #| label: my-chunk
    my_code()
    ```
    ````

This renders as `` ```{r} `` in the output without executing.

**Verbatim inline R code** — use double-backtick escaping outside any code fence: ``` `` `r expr` `` ```. This displays the literal `` `r expr` `` text without knitr executing it.

**Do NOT use** these approaches (they fail):
- 5-backtick fences wrapping `` ```{r} `` — knitr still executes the inner chunk
- HTML entities (`&#96;`) inside code fences — rendered as literal `&#96;` text
- `{verbatim}` engine with inline R — may convert backticks to HTML entities
- Plain code fences containing `` `r expr` `` or `` `{r} expr` `` — knitr still executes them

## What Not to Change

- `WECA_R_QUARTO_COURSE_PLAN.md` is the original detailed course plan reference document
- `pedagogies-for-learning-r-quarto.txt` is source research material
- WECA brand colours in `custom.scss` must match the organisational style guide
