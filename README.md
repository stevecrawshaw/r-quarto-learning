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

- [ ] Software installed (R, Positron, Quarto, Git, Python, uv)
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

# Render the training book
quarto render

# Or preview with live reload
quarto preview
```

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
├── resources/             # Reference materials
│   ├── datasets.qmd       # Practice dataset documentation
│   ├── setup-guide.qmd    # Installation and setup
│   └── troubleshooting.qmd # Common issues and solutions
├── data/                  # Example datasets
│   └── examples/          # Practice data for exercises
└── _output/               # Rendered HTML (gitignored)
```

## Learning Outcomes

By the end of this course, you will be able to:

- Navigate the command line (Git Bash) for basic file operations
- Use Positron IDE to write and execute R code
- Load, transform, and analyse data using tidyverse packages
- Create publication-quality visualisations with ggplot2
- Author reproducible reports combining code, narrative, and outputs using Quarto
- Use Git for version control and GitHub for collaboration
- Follow the WECA indicators project workflow independently

## Course Philosophy

This course follows evidence-based pedagogical principles:

1. **"Whole Game First"** - Experience the complete workflow before diving into details
2. **Tidyverse-First** - Human-centered R syntax from the start
3. **Visual Feedback Early** - Create charts in Session 1 for immediate gratification
4. **Real-World Application** - Build actual WECA indicators, not toy examples
5. **Literate Programming** - Code + narrative from day one via Quarto
6. **Active Learning** - Live coding, immediate practice, pair programming
7. **Low Friction** - Pre-installed software, standardized helper functions

## Resources

- [Course materials (rendered)](https://your-site.com)
- [Indicators project repository](https://github.com/your-org/indicators)
- [R for Data Science](https://r4ds.hadley.nz/)
- [Quarto documentation](https://quarto.org/docs/guide/)
- [Git documentation](https://git-scm.com/doc)

## Support

- **Team chat:** `#indicators-training` channel
- **Office hours:** Wednesdays, 2-3pm
- **Instructor:** [Name] - [email]

## Contributing

Suggestions for improving the training materials are welcome! Please:

1. Open an issue describing the improvement
2. Or submit a pull request with changes
3. Or discuss in the `#indicators-training` channel

## License

This training material is developed for internal WECA use. For questions about reuse or adaptation, contact [your-team@example.com].

---

*Part of the WECA Analysis & Evaluation training program*
