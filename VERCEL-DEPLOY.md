# Vercel Deployment Guide

This site is pre-rendered locally with Quarto and auto-deployed to Vercel on push.

## Setup

- **Repo:** `stevecrawshaw/r-quarto-learning`
- **Root Directory (in Vercel settings):** `.` (repo root — leave as default)
- **Framework Preset:** Other
- **Build Command:** Leave empty / override to none
- **Output Directory:** `_output` (configured in `vercel.json`)

## Deployment Workflow

1. Make content changes to `.qmd` files
2. Render locally: `quarto render`
3. Commit the changes including the updated `_output/` directory
4. Push to GitHub — Vercel auto-deploys

## Key Files

| File | Purpose |
|------|---------
| `vercel.json` | Tells Vercel to serve `_output/` with no build step |
| `_quarto.yml` | Quarto config; output dir is `_output` |
| `.gitignore` | `_output/` is **not** ignored so rendered files are committed |

## Notes

- No build tools or runtimes are needed on Vercel — it just serves the static files.
