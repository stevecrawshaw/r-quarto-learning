# Prompt: Bash Command Learning Playground

Use this prompt with Claude Code's `/playground` skill to generate an interactive HTML playground for learning bash/terminal commands.

---

Create an interactive playground for learning essential bash/terminal commands aimed at analysts who are new to the command line. The target audience are WECA analysts learning R, Quarto, and Git who need enough terminal fluency to navigate files, run scripts, and use Git confidently.

## Scope

Focus on the commands a data analyst actually needs day-to-day, not sysadmin tasks. Group them into these areas:

1. **Navigation** — `pwd`, `cd`, `ls` (with `-l`, `-a` flags), `~` and `..` shortcuts
2. **Files & folders** — `mkdir`, `touch`, `cp`, `mv`, `rm`, `rmdir`, understanding paths (absolute vs relative)
3. **Reading files** — `cat`, `head`, `tail`, `less` (conceptually), `wc`
4. **Finding things** — `find` (basic usage), `grep` (search within files)
5. **Pipes & redirection** — `|`, `>`, `>>`, chaining commands together
6. **Practical essentials** — `echo`, `which`, `man` (conceptually), `clear`, `history`, tab completion (explain conceptually)

## Design

Model this on the git-learning-playground.html in this repo. Specifically:

### Layout

- **Left sidebar**: Lesson list with completion tracking, current task hint box with explanatory text, quick reference of commands
- **Centre top**: A visual file tree that updates live as the user creates, moves, and deletes files and folders. Show the current working directory highlighted. This replaces the commit graph from the Git playground.
- **Centre middle**: A zone showing the most recent command output (simulating what you'd see in a real terminal)
- **Centre bottom**: Terminal input where users type commands
- **Right panel**: Session summary prompt output with copy button

### Simulated filesystem

- Pre-populate with a realistic small project structure:

  ```
  ~/project/
  ├── data/
  │   ├── raw/
  │   │   └── survey_2024.csv
  │   └── clean/
  ├── scripts/
  │   ├── analysis.R
  │   └── helpers.R
  ├── output/
  ├── report.qmd
  └── README.md
  ```

- Files should have simulated content (a few lines each) so `cat`, `head`, `grep` etc. return meaningful output
- The filesystem must be fully interactive — users can create, move, copy, and delete files and the tree view updates instantly

### Lessons (6 guided lessons with rich explanatory text)

Each lesson needs:

- **Lesson introduction**: 2-3 sentences explaining the concept and why it matters for their work
- **Step explanations**: Each step has both the command to run AND an explanation covering what the command does, why you'd use it, and practical tips

#### Lesson 1: Where Am I?

Teach `pwd`, `ls`, `cd`, navigating up with `..`, and using `~` for home. Explain that the terminal is just another way to browse folders — like File Explorer but with typing instead of clicking.

#### Lesson 2: Creating & Organising

Teach `mkdir`, `touch`, `mv`, `cp`. Frame it around setting up a project folder structure — something analysts do regularly when starting new work. State that usually analysts will create new files and edit using Positron or Rstudio IDE.

#### Lesson 3: Looking at Files

Teach `cat`, `head`, `tail`, `wc`. Explain when you'd use each — `cat` for short files, `head` to peek at CSV headers, `tail` for the last few rows, `wc` to count how many rows a data file has.

#### Lesson 4: Finding Things

Teach `find` (find files by name) and `grep` (search inside files). Frame it as "your data folder has dozens of files — how do you find the one with the ONS data?" and "which of your R scripts loads the survey data?"

#### Lesson 5: Pipes & Redirection

Teach `|`, `>`, `>>`. Start with the concept: "commands are like Lego bricks — you can snap the output of one into the input of another." Refer to similarity with the R pipe |> . Show practical examples like `head -5 data.csv | wc -l` and `grep "library" scripts/*.R > dependencies.txt`.

#### Lesson 6: Putting It Together

A realistic mini-workflow: navigate to a project, see what files exist, peek at a data file, find which scripts use a particular dataset, and save the results. Mirrors what they'd do when picking up an unfamiliar project.

### Interaction details

- Tab completion simulation (show a flash/hint when user presses Tab)
- Arrow up/down for command history
- Colour-coded output: directories in blue, errors in red, command echo in green
- The file tree should use standard `├──` / `└──` characters and highlight the current directory
- Commands should handle basic flags (e.g., `ls -la`, `head -n 5 file.csv`)

### Technical requirements

- Single self-contained HTML file, all CSS and JS inline
- Dark terminal theme matching the Git playground aesthetic (use the same colour variables)
- No external dependencies
- Live-updating prompt output summarising what the user has practised
- Learn/Sandbox mode toggle

### What NOT to include

- No `sudo`, `chmod`, `chown`, or admin commands
- No package management (`apt`, `brew`, etc.)
- No scripting/bash programming (loops, variables, functions)
- No network commands (`curl`, `ssh`, `scp`)
- Keep it focused on file navigation and inspection — the commands they need for R/Quarto/Git work
