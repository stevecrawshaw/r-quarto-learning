# WECA R & Quarto Training

A 5-session [training course](https://r-quarto-learning.vercel.app/) helping WECA analysts transition from Excel/PowerPoint workflows to reproducible, code-first analysis using R, Quarto, and Git.

## Course Overview

**Duration:** 5 sessions × 4 hours (20 hours total)
**Format:** In-person, consecutive weeks
**Audience:** Analysts building indicator chapters for the regional priorities report

### Sessions

1. **The Whole Game** - Experience the complete workflow
2. **R Fundamentals** - Master data transformation and visualisation
3. **Data Wrangling** - Clean and prepare real-world data
4. **Quarto Mastery** - Author professional reproducible reports
5. **Git Collaboration** - Version control and code review

## Getting Started

### Prerequisites

Before Session 1, ensure you have:

- [ ] Software installed (R, RStudio, Quarto, Git)
- [ ] Indicators project cloned
- [ ] R packages installed (`renv::restore()`)
- [ ] Python environment set up (`uv sync`)
- [ ] Pre-commit hooks installed

See [Setup Guide](https://your-site.com/resources/setup-guide.html) for detailed instructions.

### Quick Start

```bash
# Clone this repository
git clone https://github.com/your-org/r-quarto-learning.git
cd r-quarto-learning

# Render the training book (HTML)
quarto render

# Or preview with live reload
quarto preview

# Render a WECA-branded PDF (typst)
uv run scripts/build_typst_report.py
```

The PDF script assembles all chapters into a single `training-report.pdf` in the project root. It strips YAML front matter from each chapter, injects chapter titles as headings, and renders using the `weca-report` typst extension. The generated `training-report.qmd` and `training-report.pdf` are excluded from git.

## Structure

```
r-quarto-learning/
├── index.qmd              # Landing page
├── _quarto.yml            # Book configuration
├── overview/              # Course design and pedagogy
│   ├── course-plan.qmd
│   └── pedagogy.qmd
├── sessions/              # Session-by-session materials
│   ├── session-01.qmd     # The Whole Game
│   ├── session-02.qmd     # R Fundamentals
│   ├── session-03.qmd     # Data Wrangling
│   ├── session-04.qmd     # Quarto Mastery
│   └── session-05.qmd     # Git Collaboration
├── playgrounds/           # Interactive learning simulators
│   ├── bash-learning-playground.html  # Terminal command playground
│   └── git-learning-playground.html   # Git & GitHub playground
├── resources/             # Reference materials
│   ├── datasets.qmd       # Practice dataset documentation
│   ├── setup-guide.qmd    # Installation and setup
│   └── troubleshooting.qmd # Common issues and solutions
├── data/                  # Example datasets
│   └── examples/          # Practice data for exercises
├── _extensions/           # Quarto extensions
│   └── weca-report/       # WECA-branded typst template
├── scripts/               # Build scripts
│   └── build_typst_report.py  # Assembles chapters into typst PDF
└── _output/               # Rendered HTML (committed for Vercel deploy)
```

## Learning Outcomes

By the end of this course, you will be able to:

- Navigate the command line (Git Bash) for basic file operations
- Use RStudio IDE to write and execute R code
- Load, transform, and analyse data using tidyverse packages
- Create publication-quality visualisations with ggplot2
- Author reproducible reports combining code, narrative, and outputs using Quarto
- Use Git for version control and GitHub for collaboration
- Follow the WECA indicators project workflow independently

## Course Philosophy

This course follows evidence-based pedagogical principles:

1. **"Whole Game First"** - Experience the complete workflow before diving into details
2. **Tidyverse-First** - Human-centred R syntax from the start
3. **Visual Feedback Early** - Create charts in Session 1 for immediate gratification
4. **Real-World Application** - Build actual WECA indicators, not toy examples
5. **Literate Programming** - Code + narrative from day one via Quarto
6. **Active Learning** - Live coding, immediate practice, pair programming
7. **Low Friction** - Pre-installed software, standardised helper functions

## Interactive Playgrounds

Self-contained browser-based simulators for practising commands in a safe sandbox — no installation required.

- **[Bash Learning Playground](https://r-quarto-learning.vercel.app/playgrounds/bash-learning-playground.html)** — 6 guided lessons covering navigation, file management, reading files, finding things, pipes & redirection. Uses a simulated WECA project filesystem.
- **[Git Learning Playground](https://r-quarto-learning.vercel.app/playgrounds/git-learning-playground.html)** — Interactive Git and GitHub simulator covering commits, branches, merging, and pull requests.

Both include Learn mode (step-by-step lessons) and Sandbox mode (free exploration).

## Resources

- [Course materials (rendered)](https://r-quarto-learning.vercel.app/)
- [Indicators project repository](https://github.com/westofengland-ca/weca_regional_indicators)
- [R for Data Science](https://r4ds.hadley.nz/)
- [Quarto documentation](https://quarto.org/docs/guide/)
- [Git documentation](https://git-scm.com/doc)
- [Steve's Getting Started Bookmarks](https://raindrop.io/murrayjarvis/beginner-resources-r-tidyverse-quarto-git-and-bash-67078609)

## Contributing

Suggestions for improving the training materials are welcome! Please:

1. Open an issue describing the improvement
2. Or submit a pull request with changes
3. Or discuss in the `Analysts team chat` Teams channel

## Licence

This training material is developed for internal WECA use. For questions about reuse or adaptation, raise an issue in this repo.

---
