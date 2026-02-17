# WECA Indicators: R & Quarto Training Course

**Duration:** 5 sessions × 4 hours (20 hours total instruction)
**Format:** In-person, consecutive weeks
**Audience:** 5 analysts transitioning from Excel/PowerPoint to code-first analysis
**Goal:** Enable each analyst to independently create indicator chapters using R, Quarto, and Git

---

## Course Design Philosophy

This course follows evidence-based pedagogical principles:

1. **"Whole Game First"** - Session 1 shows the complete workflow before diving into details
2. **Tidyverse-First** - Human-centered R syntax (pipes, verbs) from the start
3. **Visual Feedback Early** - Charts in Session 1 for immediate gratification
4. **Real-World Application** - Build actual WECA indicators, not toy examples
5. **Literate Programming** - Code + narrative from day one via Quarto
6. **Active Learning** - Live coding, immediate practice, pair programming options
7. **Low Friction** - Pre-installed software, standardized helper functions

---

## Learning Outcomes

By the end of this course, analysts will be able to:

- Navigate the command line (Git Bash) for basic file operations
- Use Positron IDE to write and execute R code
- Load, transform, and analyze data using tidyverse packages
- Create publication-quality visualizations with ggplot2
- Author reproducible reports combining code, narrative, and outputs using Quarto
- Use Git for version control and GitHub for collaboration
- Follow the WECA indicators project workflow independently

---

## Course Overview

| Session | Focus | Key Milestone |
|---------|-------|---------------|
| **1** | The Whole Game | Render a complete indicator from template |
| **2** | R Fundamentals | Transform and visualize real data |
| **3** | Data Wrangling | Clean and prepare messy datasets |
| **4** | Quarto Mastery | Author professional multi-section reports |
| **5** | Git Collaboration | Create, review, and merge pull requests |

---

## Pre-Session Setup (Instructor)

**Week Before Session 1:**

1. Install software on all machines:
   - Positron, R (≥4.3), Python (≥3.10), Quarto (≥1.4), Git, uv
2. Clone `indicators` repository to `~/projects/` on each machine
3. Run setup scripts:
   - `./scripts/install-hooks.sh` (pre-commit hooks)
   - `renv::restore()` in R (packages)
   - `uv sync` in terminal (Python environment)
4. Prepare 5 example datasets (CSV files) in `data/examples/`:
   - Simple, clean data (4-6 columns, 20-50 rows)
   - Topics relevant to each priority area (transport, economy, skills, etc.)
   - Variables ready for plotting (year, value, category)
5. Create practice branches for each analyst: `firstname-practice`

---

# Session 1: The Whole Game (4 hours)

**Goal:** Experience the complete workflow - from data to published report - to understand *why* we're learning each tool.

## Learning Outcomes

- Understand the "code-first" analysis paradigm vs. Excel workflows
- Navigate the indicators project structure
- Execute an R code chunk in Quarto
- Render a chapter to HTML
- See the role of Git in version control (conceptual)

## Session Structure

### Part 1: Welcome & Context (30 min)

**Why are we here?**

- The limitations of Excel/PowerPoint workflows (manual updates, copy-paste errors, unclear provenance)
- Benefits of code-first analysis: reproducibility, automation, transparency, collaboration
- Tour of the final product: rendered indicators book

**The tools we'll learn:**

- **Git Bash**: Command-line interface (the "steering wheel")
- **Positron**: Integrated development environment (the "dashboard")
- **R**: Statistical programming language (the "engine")
- **Quarto**: Literate programming system (the "publishing press")
- **Git/GitHub**: Version control (the "time machine + collaboration hub")

**Analogy:** If analysis were cooking:

- Excel is a microwave meal kit
- Code-first is a professional kitchen with recipes you can modify, share, and improve

### Part 2: The Whole Game Walkthrough (90 min)

**Live Demonstration (30 min)** - Instructor creates an indicator from scratch:

1. Open Positron
2. Navigate to `chapters/02-transport/index.qmd`
3. Write a simple R code chunk:

   ```r
   library(tidyverse)
   source(here::here("scripts", "R", "theme_weca.R"))

   # Load example data
   bus_data <- read_csv("data/examples/bus_ridership.csv")

   # Create visualization
   ggplot(bus_data, aes(x = year, y = ridership)) +
     geom_line(colour = get_weca_color("forest_green"), linewidth = 1.2) +
     geom_point(colour = get_weca_color("forest_green"), size = 3) +
     theme_weca() +
     labs(title = "Annual Bus Ridership",
          x = "Year",
          y = "Ridership (millions)")
   ```

4. Execute chunk (Ctrl+Shift+Enter)
5. Render chapter (Quarto: Render button)
6. View output in browser

**Guided Practice (60 min)** - Analysts follow along:

*Note: Pair programming optional here - analysts can work individually or pair up*

1. Open Positron (show how to launch from Start menu)
2. Open project: `File > Open Project > indicators/indicators.Rproj`
3. Open their assigned example chapter (pre-created templates)
4. Execute the setup chunk (walk through line-by-line what it does)
5. Modify the plot title and colors
6. Re-render and view changes

**Common Issues Troubleshooting (built into this time):**

- Package not found → `renv::restore()`
- File path errors → Emphasize `here::here()`
- Rendering fails → Check R console for errors

**BREAK (15 min)**

### Part 3: Understanding the Pieces (45 min)

**Project Structure Tour (15 min):**
Walk through the directory tree (use File Explorer + Positron's file panel):

```
indicators/
├── chapters/           # Your work goes here
│   ├── 01-economy/
│   ├── 02-transport/
│   └── ...
├── data/
│   ├── raw/           # Original data files
│   ├── processed/     # Cleaned data
│   └── examples/      # Practice datasets
├── scripts/
│   └── R/             # Shared helper functions
├── _quarto.yml        # Book configuration
└── .git/              # Version control (hidden)
```

**Code Chunk Anatomy (15 min):**
Dissect the code they just ran:

```r
#| label: my-chart           # Unique identifier
#| fig-cap: "Description"    # Figure caption

library(tidyverse)           # Load tools
data <- read_csv("file.csv") # Import data
ggplot(data, aes(x, y)) +    # Visualize
  geom_line()
```

**Quarto Rendering Process (15 min):**

- Markdown → formatted text
- Code chunks → executed by R → output
- Combined → HTML/PDF

Show the "Source" vs. "Visual" editor modes in Positron.

### Part 4: Your First Modification (60 min)

**Individual Exercise:**

Each analyst modifies their example indicator:

1. Change the chart title to something descriptive
2. Change the line color to `"claret"` (show `show_weca_palette()`)
3. Add a subtitle using the `subtitle` argument in `labs()`
4. Add a text section above the chart explaining what it shows
5. Re-render and verify changes

**Stretch Goal** (for faster learners):

- Add a second chart using `geom_point()` or `geom_col()`
- Filter the data to show only recent years using `filter(year >= 2020)`

**Instructor:** Circulate, answer questions, help with errors. Expect file path issues, typos, and R syntax confusion.

### Part 5: Wrap-up & Homework (30 min)

**What We Learned Today:**

- The complete workflow: data → code → chart → report
- How to run R code in Quarto
- How to render a chapter
- The WECA project structure

**Looking Ahead:**

- Session 2: Deep dive into R syntax and data manipulation
- Session 3: Cleaning messy data
- Session 4: Advanced Quarto features
- Session 5: Git collaboration

**Homework (1-2 hours):**

1. **Read:** GETTING_STARTED.md sections on "Prerequisites" and "First-Time Setup"
2. **Watch:** (Provide link to 15-min video on "What is the Tidyverse?")
3. **Practice:** Modify your example indicator chapter:
   - Add a second visualization (bar chart or scatter plot)
   - Write 2-3 sentences describing what the data shows
   - Experiment with different WECA colors
4. **Explore:** Open `scripts/R/helpers.R` and read the function documentation
5. **Prepare:** Come with one question about something that confused you today

**Optional Reading:**

- R for Data Science: Chapter 1 (Introduction)
- Quarto Guide: "Hello, Quarto" tutorial

---

# Session 2: R Fundamentals (4 hours)

**Goal:** Gain confidence with R syntax, data transformation, and visualization using the tidyverse.

## Learning Outcomes

- Understand R's key data structure (tibble/data frame)
- Use the pipe operator (`%>%` or `|>`) to chain operations
- Apply core dplyr verbs: `filter`, `select`, `mutate`, `summarize`, `group_by`
- Create multi-layered ggplot2 visualizations
- Debug common R errors

## Session Structure

### Part 1: Homework Review & Questions (30 min)

- Show-and-tell: Volunteers demonstrate their homework modifications
- Address common questions from homework prep
- Quick poll: What was most confusing? (Adjust session focus accordingly)

### Part 2: R Basics - Data Structures (45 min)

**The Tibble: R's Spreadsheet**

Live coding demonstration in Positron's R console:

```r
# Create a simple tibble (like an Excel table)
library(tidyverse)

my_data <- tibble(
  area = c("Bristol", "Bath", "South Glos", "North Somerset"),
  population = c(463377, 88859, 285093, 213919),
  employed = c(219000, 45000, 142000, 98000)
)

# View it
my_data

# Access a column
my_data$population

# Calculate employment rate
my_data$employment_rate <- my_data$employed / my_data$population

# View updated data
my_data
```

**Key Concepts:**

- Tibbles are like Excel tables with named columns
- `<-` means "assign to" (store a value)
- `$` accesses a column
- R is case-sensitive: `Population` ≠ `population`
- Comments start with `#`

**Guided Practice (15 min):**
Analysts create their own tibble with 3-4 rows of made-up indicator data (year, value, category).

### Part 3: The Tidyverse Way - Verbs and Pipes (60 min)

**BREAK (15 min)**

**The Pipe Operator** - Making code readable:

```r
# Old way (nested, hard to read)
summarize(filter(my_data, population > 100000),
          mean_pop = mean(population))

# Tidyverse way (sequential, readable)
my_data %>%
  filter(population > 100000) %>%
  summarize(mean_pop = mean(population))
```

**Analogy:** Pipes are like assembly lines - each step does one thing clearly.

**The Five Core Verbs** (teach one at a time with immediate practice):

**1. `filter()` - Keep rows that match a condition**

```r
bus_data %>%
  filter(year >= 2020)  # Only recent years

bus_data %>%
  filter(ridership > 50, region == "Bristol")  # Multiple conditions
```

*Practice:* Filter your example data to show only values above a certain threshold.

**2. `select()` - Keep specific columns**

```r
bus_data %>%
  select(year, ridership, route)  # Keep these columns

bus_data %>%
  select(-notes)  # Drop the notes column
```

*Practice:* Select only the columns needed for your chart.

**3. `mutate()` - Create new columns**

```r
bus_data %>%
  mutate(
    ridership_millions = ridership / 1000000,
    pct_change = (ridership - lag(ridership)) / lag(ridership) * 100
  )
```

*Practice:* Create a new column that calculates a percentage or ratio.

**BREAK (15 min)**

**4. `summarize()` - Calculate summary statistics**

```r
bus_data %>%
  summarize(
    total = sum(ridership),
    average = mean(ridership),
    max_year = max(year)
  )
```

**5. `group_by()` - Do calculations by category**

```r
bus_data %>%
  group_by(region) %>%
  summarize(
    avg_ridership = mean(ridership),
    total_routes = n()
  )
```

*Practice (20 min):* Using one of the example datasets:

1. Filter to a date range
2. Group by category
3. Calculate the average value
4. Create a bar chart showing the result

### Part 4: ggplot2 - Grammar of Graphics (60 min)

**Building Plots Layer by Layer:**

```r
# Layer 1: Data + aesthetic mapping
ggplot(bus_data, aes(x = year, y = ridership))

# Layer 2: Add geometry (the visual representation)
ggplot(bus_data, aes(x = year, y = ridership)) +
  geom_line()

# Layer 3: Add styling
ggplot(bus_data, aes(x = year, y = ridership)) +
  geom_line(colour = "blue", linewidth = 1) +
  geom_point(size = 2)

# Layer 4: Add labels
ggplot(bus_data, aes(x = year, y = ridership)) +
  geom_line(colour = get_weca_color("forest_green"), linewidth = 1) +
  geom_point(size = 2) +
  labs(title = "Bus Ridership Over Time",
       x = "Year",
       y = "Ridership (millions)") +
  theme_weca()
```

**Key ggplot2 Geometries:**

- `geom_line()` - Line charts (trends over time)
- `geom_point()` - Scatter plots (relationships)
- `geom_col()` - Bar charts (comparisons)
- `geom_smooth()` - Trend lines

**Mapping Variables to Aesthetics:**

```r
# Color by category
ggplot(data, aes(x = year, y = value, colour = region)) +
  geom_line()

# Different line types by category
ggplot(data, aes(x = year, y = value, linetype = category)) +
  geom_line()

# Size points by value
ggplot(data, aes(x = year, y = value, size = population)) +
  geom_point()
```

**Guided Practice (30 min):**

Create three different visualizations from the same dataset:

1. Line chart showing trend over time
2. Bar chart comparing categories
3. Multi-line chart with color-coded groups

**Instructor:** Emphasize `aes()` maps *variables* to visual properties, while direct arguments (outside `aes()`) set fixed values.

### Part 5: Debugging R Errors (30 min)

**Common Error Messages and Fixes:**

1. **`could not find function "filter"`**
   - Fix: Load the library first: `library(tidyverse)`

2. **`object 'data' not found`**
   - Fix: Make sure you ran the chunk that loads the data

3. **`unexpected symbol`**
   - Fix: Check for missing commas, quotes, or parentheses

4. **`Error in xy.coords(x, y) : 'x' and 'y' lengths differ`**
   - Fix: Your data columns have different numbers of rows (check for NAs)

**Debugging Strategy:**

1. Read the error message (bottom-up in stack trace)
2. Check the line number mentioned
3. Look for typos in variable/column names
4. Run code chunk-by-chunk to isolate the problem
5. Use `View(data)` to inspect your data frame

**Practice Exercise:**
Provide code snippets with deliberate errors. Analysts fix them in pairs.

### Part 6: Wrap-up & Homework (15 min)

**Homework (1-2 hours):**

1. **Complete:** The "R Basics" chapter in R for Data Science (provided link/PDF)
2. **Practice:** Using your assigned example dataset:
   - Calculate 3 summary statistics (min, max, mean)
   - Create 2 different chart types
   - Add WECA theme and appropriate labels
3. **Create:** A new indicator section in your practice chapter that includes:
   - Data loading with `read_csv()`
   - At least one `filter()` or `mutate()` operation
   - A complete visualization
   - A paragraph describing findings
4. **Prepare:** Bring a real WECA dataset (CSV) you'd like to work with in Session 3

**Challenge Exercise** (optional):

- Use `facet_wrap()` to create small multiples (multiple charts by category)
- Add error bars or confidence intervals to your chart

---

# Session 3: Data Wrangling (4 hours)

**Goal:** Master the skills to clean, reshape, and prepare messy real-world data for analysis.

## Learning Outcomes

- Import data from CSV and Excel files
- Handle missing values and data quality issues
- Reshape data between wide and long formats
- Join multiple datasets together
- Apply data cleaning best practices
- Use the `here()` package for robust file paths

## Session Structure

### Part 1: Homework Review & Real Data Discussion (30 min)

- Volunteer demos of homework indicators
- Quick discussion: What datasets did you bring? What challenges do you anticipate?
- Preview of today's focus: preparing data for analysis

### Part 2: Importing Data (45 min)

**Reading CSV Files:**

```r
library(tidyverse)
library(readxl)  # For Excel files
source(here::here("scripts", "R", "helpers.R"))

# The WECA way - using helper function
data <- load_csv(here::here("data", "raw", "indicator_data.csv"))

# Behind the scenes (what the helper does)
data <- read_csv("data/raw/indicator_data.csv",
                 show_col_types = FALSE)
```

**Reading Excel Files:**

```r
# Basic read
data <- read_excel("data/raw/employment_data.xlsx")

# Specific sheet
data <- read_excel("data/raw/employment_data.xlsx",
                   sheet = "Q4_2024")

# Skip header rows
data <- read_excel("data/raw/employment_data.xlsx",
                   sheet = "Data",
                   skip = 5)  # Skip first 5 rows
```

**File Path Best Practices:**

```r
# ✅ Good - relative paths with here()
data <- load_csv(here::here("data", "raw", "myfile.csv"))

# ❌ Bad - absolute paths (breaks on other computers)
data <- read_csv("C:/Users/steve/projects/indicators/data/raw/myfile.csv")

# ❌ Bad - fragile relative paths (breaks if working directory changes)
data <- read_csv("../data/raw/myfile.csv")
```

**Why `here()` works:** It always starts from the project root (where `.Rproj` is), regardless of where your code file is located.

**Guided Practice (20 min):**

1. Import one of the provided example datasets using `load_csv()`
2. Import an Excel file from `data/examples/`
3. View the data with `View(data)` or `glimpse(data)`
4. Check dimensions with `nrow(data)` and `ncol(data)`

### Part 3: Data Cleaning Essentials (60 min)

**Cleaning Column Names:**

```r
library(janitor)

# Before: messy names
# "Area Name", "Year (2023)", "Percentage (%)"

data_clean <- data %>%
  clean_names()  # Converts to: area_name, year_2023, percentage

# View the changes
names(data)
names(data_clean)
```

**Handling Missing Values:**

```r
# Check for missing data
check_missing(data)

# Remove rows with ANY missing values
data_complete <- data %>%
  drop_na()

# Remove rows with missing values in specific columns
data_filtered <- data %>%
  drop_na(year, value)

# Replace missing values
data_filled <- data %>%
  mutate(
    value = if_else(is.na(value), 0, value),  # Replace NA with 0
    category = replace_na(category, "Unknown")  # Replace NA with "Unknown"
  )
```

**Type Conversions:**

```r
# Convert text to numbers
data <- data %>%
  mutate(
    year = as.numeric(year),
    value = as.numeric(value)
  )

# Convert text to dates
data <- data %>%
  mutate(
    date = as.Date(date, format = "%d/%m/%Y")  # e.g., "31/12/2023"
  )

# Convert to categories (factors)
data <- data %>%
  mutate(
    region = factor(region,
                    levels = c("Bristol", "Bath", "South Glos", "North Somerset"))
  )
```

**BREAK (15 min)**

**Dealing with Duplicates:**

```r
# Check for duplicates
data %>%
  get_dupes()  # From janitor package

# Remove duplicate rows
data_unique <- data %>%
  distinct()

# Keep only first occurrence of duplicate combinations
data_deduped <- data %>%
  distinct(year, area, .keep_all = TRUE)
```

**Filtering and Subsetting:**

```r
# Remove specific problem values
data_clean <- data %>%
  filter(
    !is.na(value),           # Remove missing values
    value > 0,               # Remove zeros/negatives
    year >= 2015,            # Only recent years
    area != "UNKNOWN"        # Exclude unknown areas
  )

# Remove outliers (values beyond 3 standard deviations)
data_no_outliers <- data %>%
  filter(
    value > mean(value) - 3 * sd(value),
    value < mean(value) + 3 * sd(value)
  )
```

**Guided Practice (30 min):**

Using one of the "messier" example datasets provided:

1. Clean the column names
2. Check for and handle missing values
3. Convert date/year columns to appropriate types
4. Remove any duplicate rows
5. Filter to a relevant subset

### Part 4: Reshaping Data (60 min)

**Understanding Wide vs. Long Format:**

Wide format (like Excel - one row per observation):

```
year  bristol_value  bath_value  sg_value
2020       1000         500        750
2021       1100         520        780
```

Long format (tidy - one row per measurement):

```
year  area            value
2020  Bristol         1000
2020  Bath             500
2020  South Glos       750
2021  Bristol         1100
2021  Bath             520
2021  South Glos       780
```

**Why Long Format?** ggplot2 and tidyverse functions work best with long format. It's easier to group, filter, and visualize.

**Pivot Longer - Wide to Long:**

```r
# Wide to long
data_long <- data_wide %>%
  pivot_longer(
    cols = bristol_value:sg_value,  # Columns to pivot
    names_to = "area",               # New column for names
    values_to = "value"              # New column for values
  )

# Clean up the area names
data_long <- data_long %>%
  mutate(
    area = str_remove(area, "_value"),  # Remove "_value" suffix
    area = str_to_title(area)            # Capitalize properly
  )
```

**Pivot Wider - Long to Wide:**

```r
# Long to wide (less common, but useful for tables)
data_wide <- data_long %>%
  pivot_wider(
    names_from = area,    # Column containing new column names
    values_from = value   # Column containing values
  )
```

**BREAK (15 min)**

**Practical Example:**

Given an Excel export with this structure:

```
Area          | 2020 | 2021 | 2022 | 2023
Bristol       | 100  | 110  | 120  | 130
Bath          | 50   | 55   | 58   | 60
```

Transform it for plotting:

```r
data_tidy <- data_wide %>%
  pivot_longer(
    cols = `2020`:`2023`,      # Year columns (backticks for numbers)
    names_to = "year",
    values_to = "value"
  ) %>%
  mutate(year = as.numeric(year))  # Convert year to number

# Now we can plot it
ggplot(data_tidy, aes(x = year, y = value, colour = Area)) +
  geom_line() +
  theme_weca()
```

**Guided Practice (30 min):**

1. Take a provided wide-format dataset
2. Pivot it to long format
3. Create a multi-line chart with different colors for each category
4. Calculate summary statistics by group

### Part 5: Joining Datasets (30 min)

**Why Join?** Combine data from multiple sources (e.g., population data + indicator data).

**Types of Joins:**

```r
# Left join - keep all rows from first table, match from second
combined <- data1 %>%
  left_join(data2, by = "area")

# Inner join - keep only rows that match in both
combined <- data1 %>%
  inner_join(data2, by = "area")

# Join on multiple columns
combined <- data1 %>%
  left_join(data2, by = c("area", "year"))
```

**Practical Example:**

```r
# Load indicator data
indicator_data <- load_csv(here::here("data", "raw", "employment.csv"))

# Load population data
population_data <- load_csv(here::here("data", "raw", "population.csv"))

# Combine them to calculate rates
combined_data <- indicator_data %>%
  left_join(population_data, by = c("area", "year")) %>%
  mutate(
    employment_rate = safe_divide(employed, population) * 100
  )
```

**Guided Practice (15 min):**
Join two provided datasets and calculate a derived metric.

### Part 6: Real Data Workshop (45 min)

**Hands-On Exercise:**

Analysts work with their own real WECA datasets (or instructor-provided messy datasets):

1. Import the data
2. Inspect and document issues (`check_missing()`, `glimpse()`)
3. Clean column names
4. Handle missing values appropriately
5. Reshape if needed (wide to long)
6. Create a simple visualization
7. Calculate summary statistics

**Instructor:** Circulate and provide individualized guidance. Common issues will include date formats, column name encoding, and choosing appropriate NA handling strategies.

**Stretch Goal:** Join with a second dataset if analysts brought multiple files.

### Part 7: Wrap-up & Homework (15 min)

**Homework (1-2 hours):**

1. **Complete:** Prepare your real indicator data for analysis:
   - Import and clean the dataset
   - Document data quality issues in comments
   - Create a cleaned version saved to `data/processed/`
   - Create one exploratory visualization

2. **Create:** A draft indicator section that includes:
   - Data loading and cleaning code (with comments explaining decisions)
   - At least one transformation (calculate rate, percentage, change)
   - One publication-ready chart with proper labels
   - A findings paragraph describing what the data shows

3. **Read:** CONTRIBUTING.md sections on "Code Style Guide" and "File Naming Conventions"

4. **Optional Challenge:**
   - Join your indicator data with population or geographic data
   - Create a grouped/faceted visualization showing multiple areas or categories

---

# Session 4: Quarto Mastery (4 hours)

**Goal:** Author professional, reproducible reports that combine narrative, code, visualizations, and tables.

## Learning Outcomes

- Structure multi-section Quarto documents
- Control code chunk execution and output
- Format text with Markdown syntax
- Create professional tables
- Use cross-references for figures and tables
- Understand the "freeze" workflow for collaboration
- Render both HTML and PDF outputs

## Session Structure

### Part 1: Homework Review (30 min)

- Show-and-tell: Volunteers share their cleaned datasets and draft indicators
- Discussion: What data cleaning challenges did you encounter?
- Quick troubleshooting session for common issues

### Part 2: Markdown Essentials (45 min)

**Why Markdown?** Plain text formatting that's readable as code but renders beautifully.

**Basic Syntax:**

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another point
  - Nested point

1. Numbered list
2. Second item

[Link text](https://example.com)

![Image caption](path/to/image.png)

> Block quote - for highlighting key findings

`inline code` for variable names like `employment_rate`
```

**Formatted Output Examples:**
Show side-by-side comparison of Markdown source and rendered HTML.

**Guided Practice (20 min):**

In your practice chapter:

1. Add section headings (##, ###)
2. Format key numbers in bold
3. Create a bulleted list of findings
4. Add a block quote highlighting the main insight
5. Render and view the formatted output

### Part 3: Quarto Code Chunks (60 min)

**Anatomy of a Code Chunk:**

````markdown
```{r}
#| label: my-analysis
#| echo: false
#| warning: false
#| message: false
#| fig-cap: "Employment trends across the region"
#| fig-width: 8
#| fig-height: 5

# Your R code here
ggplot(data, aes(x = year, y = value)) +
  geom_line() +
  theme_weca()
```
````

**Key Chunk Options:**

| Option | Effect | When to Use |
|--------|--------|-------------|
| `echo: false` | Hide code, show output | Final reports (code is distracting) |
| `echo: true` | Show code and output | Teaching, documentation |
| `eval: false` | Show code, don't run | Example code, broken code to fix later |
| `include: false` | Run code, hide everything | Setup chunks, data loading |
| `warning: false` | Suppress warnings | Known harmless warnings |
| `message: false` | Suppress messages | Package loading messages |
| `fig-cap: "..."` | Figure caption | All charts (for accessibility) |
| `fig-width: 8` | Figure width (inches) | Customize chart size |
| `label: my-chunk` | Chunk identifier | Required for cross-references |

**BREAK (15 min)**

**Code Folding** (already enabled in `_quarto.yml`):

Readers can toggle code visibility with "Show code" buttons. Best of both worlds: clean reading experience + transparency.

**Conditional Execution:**

````markdown
```{r}
#| eval: false
#| code-summary: "Code to load data (not run in this demo)"

# This code is shown but not executed
data <- load_csv("path/to/large/file.csv")
```
````

**BREAK (15 min)**

**Inline R Code:**

Instead of copying numbers from R output into your text, compute them inline:

```markdown
The employment rate increased from
`r min(data$employment_rate)`% in 2015 to
`r max(data$employment_rate)`% in 2024,
a change of `r format_number(pct_change(max(data$employment_rate),
                                         min(data$employment_rate)),
                              digits = 1)`%.
```

**Renders as:**
"The employment rate increased from 72.3% in 2015 to 78.5% in 2024, a change of 8.6%."

**Benefits:**

- Numbers update automatically when data changes
- No copy-paste errors
- Ensures text matches visualizations

**Guided Practice (30 min):**

Enhance your draft indicator:

1. Add appropriate chunk options to hide setup code
2. Show only your analysis code (with `code-fold: true`)
3. Add figure captions to all charts
4. Use inline R code to report key statistics in your narrative
5. Re-render and verify all numbers are correct

### Part 4: Tables in Quarto (45 min)

**Creating Simple Tables with Markdown:**

```markdown
| Area | Population | Employment Rate |
|------|------------|-----------------|
| Bristol | 463,377 | 76.2% |
| Bath | 88,859 | 79.1% |
| South Glos | 285,093 | 78.5% |
```

**Creating Tables from Data with `knitr::kable()`:**

```r
# Basic table
data %>%
  select(area, population, employment_rate) %>%
  knitr::kable()

# Formatted table with custom column names
data %>%
  select(area, population, employment_rate) %>%
  knitr::kable(
    col.names = c("Area", "Population", "Employment Rate (%)"),
    digits = 1,
    format.args = list(big.mark = ",")
  )
```

**Summary Tables:**

```r
# Use the helper function
data %>%
  summary_table(group_var = "area", value_var = "employment_rate") %>%
  knitr::kable(digits = 1)
```

**Advanced: gt Package for Publication Tables:**

```r
library(gt)

data %>%
  group_by(area) %>%
  summarise(
    avg_rate = mean(employment_rate),
    min_rate = min(employment_rate),
    max_rate = max(employment_rate)
  ) %>%
  gt() %>%
  tab_header(title = "Employment Rate Summary by Area") %>%
  cols_label(
    area = "Area",
    avg_rate = "Average",
    min_rate = "Minimum",
    max_rate = "Maximum"
  ) %>%
  fmt_number(columns = c(avg_rate, min_rate, max_rate), decimals = 1)
```

**Guided Practice (20 min):**
Create a summary table showing key statistics for your indicator (min, max, average, latest value).

### Part 5: Document Structure & Cross-References (45 min)

**YAML Frontmatter:**

```yaml
---
title: "Public Transport Connectivity"
subtitle: "Connecting the region through better public transport"
author: "Your Name"
date: last-modified
execute:
  echo: true
  warning: false
  message: false
---
```

**Document Sections:**

```markdown
## Context
[Background and importance]

## Data Sources
[Describe data provenance]

## Indicator 1: Bus Ridership

### Overview
[What this measures]

### Analysis
[Charts and findings]

### Key Findings
[Bullet points of insights]

## Indicator 2: Network Coverage
[Repeat structure]

## Summary
[Overall conclusions]
```

**Cross-References to Figures:**

````markdown
```{r}
#| label: fig-employment-trend
#| fig-cap: "Employment rate trends 2015-2024"

ggplot(data, aes(x = year, y = employment_rate)) +
  geom_line() +
  theme_weca()
```

As shown in @fig-employment-trend, employment rates have
steadily increased over the past decade.
````

**Cross-References to Tables:**

````markdown
```{r}
#| label: tbl-summary
#| tbl-cap: "Summary statistics by area"

data %>%
  summary_table(group_var = "area", value_var = "employment_rate") %>%
  knitr::kable()
```

@tbl-summary presents the employment rate statistics for each area.
````

**Guided Practice (20 min):**

1. Add proper YAML frontmatter to your chapter
2. Organize content into logical sections with headings
3. Add labels and captions to all figures
4. Add at least one cross-reference to a figure in your text

### Part 6: The Freeze Workflow for Collaboration (30 min)

**The Problem:** Each analyst has different data on their machine. How do we render the full book without everyone's data?

**The Solution:** Quarto's `freeze: auto` mode (already configured in `_quarto.yml`).

**How It Works:**

1. You render your chapter with your local data
2. Quarto saves the outputs (plots, tables) to `_freeze/` directory
3. You commit both source (`.qmd`) and cache (`_freeze/`) to Git
4. Others pull your changes and render the full book using your cached outputs
5. Their Quarto skips re-executing your code - uses your cached results

**Workflow in Practice:**

```bash
# After editing your chapter
quarto render chapters/02-transport/index.qmd

# Commit BOTH source and cache
git add chapters/02-transport/index.qmd
git add _freeze/html/chapters/02-transport/
git commit -m "Add bus ridership indicator"
git push
```

**Important:** Always commit the `_freeze/` directory alongside your `.qmd` file!

**When to Force Re-render:**

```bash
# If your data updated but source code didn't change
quarto render chapters/02-transport/index.qmd --execute-freeze refresh
```

**Visual Demonstration:**

- Show the `_freeze/` directory structure
- Demonstrate how editing text (not code) doesn't trigger re-execution
- Show what happens when someone forgets to commit `_freeze/` (error demo)

### Part 7: Rendering Options (15 min)

**HTML vs. PDF:**

```bash
# HTML (default, configured in _quarto.yml)
quarto render chapters/02-transport/index.qmd

# PDF (useful for printing/archiving)
quarto render chapters/02-transport/index.qmd --to pdf

# Both formats
quarto render chapters/02-transport/index.qmd --to all
```

**Rendering the Full Book:**

```bash
# From project root
quarto render

# Preview with live reload (auto-updates as you edit)
quarto preview
```

**Preview vs. Render:**

- **Preview:** Opens browser, watches for changes, auto-reloads
- **Render:** One-time build of HTML/PDF files

### Part 8: Practical Exercise (45 min)

**Challenge: Create a Complete Indicator Section**

Using your real data from Session 3, create a professional indicator section that includes:

1. **YAML frontmatter** with title, author, date
2. **Context section** explaining what the indicator measures (3-4 sentences)
3. **Data section** with:
   - Code chunk loading and cleaning data (code folded)
   - Inline R code reporting dataset dimensions
4. **Analysis section** with:
   - At least two visualizations (with captions)
   - One summary table
   - Cross-references to figures in narrative text
5. **Key Findings section** with:
   - Bulleted list of 3-5 insights
   - Inline R code reporting specific values
   - Block quote highlighting the main finding
6. **Data source** citation at the end

**Success Criteria:**

- Document renders without errors
- All code chunks have labels
- All figures have captions
- Text includes at least 3 inline R computations
- Professional appearance with WECA branding

**Instructor:** Circulate, help with chunk options, cross-references, and formatting issues.

### Part 9: Wrap-up & Homework (15 min)

**Homework (1-2 hours):**

1. **Complete:** Your indicator section following the structure from the practical exercise
2. **Create:** A second indicator using a different dataset or subset
3. **Refine:**
   - Ensure all charts have descriptive titles and captions
   - Add inline R code to key statistics in your narrative
   - Check that cross-references work correctly
4. **Read:** CONTRIBUTING.md sections on "Collaborative Rendering: How the Freeze Workflow Works"
5. **Prepare:** For Session 5, ensure your chapter is render-ready and you're comfortable with the structure

**Optional Challenge:**

- Create a PDF version of your chapter
- Experiment with different WECA color schemes
- Add a custom CSS style to your chapter

---

# Session 5: Git Collaboration (4 hours)

**Goal:** Use Git and GitHub for version control, collaboration, and code review in the WECA indicators project.

## Learning Outcomes

- Understand version control concepts (commits, branches, merges)
- Use Git Bash for basic version control operations
- Create and switch between branches
- Stage, commit, and push changes
- Create and review pull requests on GitHub
- Resolve basic merge conflicts
- Follow the WECA project Git workflow

## Session Structure

### Part 1: Homework Review & Version Control Intro (45 min)

**Show-and-tell (20 min):**
Volunteers present their completed indicator sections. Highlight good examples of:

- Clear narrative structure
- Effective visualizations
- Proper use of cross-references
- Professional formatting

**Why Version Control? (25 min)**

**The Problem Without Version Control:**

```
indicator_analysis_v1.qmd
indicator_analysis_v2.qmd
indicator_analysis_v2_final.qmd
indicator_analysis_v2_final_ACTUAL.qmd
indicator_analysis_v2_final_steve_edits.qmd
```

Issues:

- Which is the current version?
- What changed between versions?
- How do we merge two people's edits?
- How do we go back if we break something?

**Version Control Solutions:**

- **Track changes** over time (like Track Changes in Word, but better)
- **Collaborate** without file conflicts
- **Revert** to previous versions if needed
- **Understand** who changed what and why
- **Branch** to experiment without breaking the main work

**Git Concepts:**

| Concept | Analogy | Purpose |
|---------|---------|---------|
| **Repository** | Project folder + time machine | Contains all files + history |
| **Commit** | Snapshot/checkpoint | Save point you can return to |
| **Branch** | Parallel timeline | Work on features without affecting main |
| **Merge** | Combine timelines | Integrate your work back to main |
| **Remote (GitHub)** | Cloud backup + collaboration hub | Share work, collaborate |

### Part 2: Git Basics in Git Bash (60 min)

**Opening Git Bash:**

- Right-click in project folder → "Git Bash Here"
- Or: Start menu → Git Bash → `cd ~/projects/indicators`

**Essential Commands:**

**1. Check Status (What's changed?)**

```bash
git status
```

Shows:

- Modified files (red = unstaged, green = staged)
- New files (untracked)
- Current branch

**2. View Changes (What exactly changed?)**

```bash
# See all changes
git diff

# See changes in a specific file
git diff chapters/02-transport/index.qmd
```

**3. Stage Changes (Prepare to commit)**

```bash
# Stage a specific file
git add chapters/02-transport/index.qmd

# Stage multiple files
git add chapters/02-transport/index.qmd _freeze/html/chapters/02-transport/

# Stage all changes (be careful!)
git add .
```

**4. Commit (Create a snapshot)**

```bash
# Commit with a message
git commit -m "Add bus ridership indicator to transport chapter"

# See commit history
git log --oneline
```

**5. Push (Upload to GitHub)**

```bash
# Push to remote
git push
```

**BREAK (15 min)**

**Guided Practice (30 min):**

Each analyst practices the basic workflow:

1. Open Git Bash in the indicators project
2. Make a small change to their chapter (add a sentence)
3. Check status: `git status`
4. View changes: `git diff`
5. Stage the file: `git add chapters/XX-topic/index.qmd`
6. Check status again: `git status` (should be green now)
7. Commit: `git commit -m "Update chapter introduction"`
8. View history: `git log --oneline`

**Do NOT push yet** - we'll cover branching first!

**Common Git Bash Tips:**

- Use Tab for autocomplete (type `cha` + Tab → completes to `chapters/`)
- Use arrow keys to recall previous commands
- `pwd` shows current directory
- `ls` lists files
- `cd` changes directory

### Part 3: Branching Workflow (60 min)

**Why Branches?**

- Work on your indicator without affecting others
- Experiment safely (can always delete the branch)
- Required for pull request workflow

**Branch Naming Convention:**

```
yourname/chapter-or-feature

Examples:
heather/transport
alex/environment-update
sarah/fix-chart-colors
```

**Creating and Using Branches:**

```bash
# See current branch (has * next to it)
git branch

# Create and switch to new branch
git checkout -b yourname/transport

# Verify you're on the new branch
git branch

# Make changes, stage, and commit as usual
git add chapters/02-transport/index.qmd
git commit -m "Add bus ridership indicator"

# Push branch to GitHub
git push -u origin yourname/transport
```

**Switching Between Branches:**

```bash
# Switch to main branch
git checkout main

# Switch back to your feature branch
git checkout yourname/transport

# List all branches (local and remote)
git branch -a
```

**Important:** Always commit or stash changes before switching branches!

**BREAK (15 min)**

**Guided Practice (30 min):**

Each analyst creates their own branch for their indicator work:

1. Ensure all current changes are committed
2. Create a new branch: `git checkout -b firstname/chapter-name`
3. Verify branch: `git branch` (should show your new branch with *)
4. Make a change to your chapter (add/modify content)
5. Stage and commit the change
6. Push the branch: `git push -u origin firstname/chapter-name`
7. Switch to main: `git checkout main` (verify chapter change disappears in Positron)
8. Switch back: `git checkout firstname/chapter-name` (verify change reappears)

**Instructor:** This concept is often confusing. Use visual aids (draw branch diagrams on whiteboard) and be prepared for many questions.

### Part 4: Pull Requests on GitHub (60 min)

**What is a Pull Request?**
A formal request to merge your branch into main. It enables:

- Code review before merging
- Discussion and feedback
- Quality control
- Documentation of changes

**Creating a Pull Request:**

**Step 1: Push Your Branch (already done in practice above)**

**Step 2: Go to GitHub**

```
https://github.com/your-org/indicators
```

You'll see a banner: "firstname/chapter-name had recent pushes" with button "Compare & pull request"

**Step 3: Fill in PR Template**

**Title:**

```
Add bus ridership indicator to transport chapter
```

**Description:**

```markdown
## Summary
Adds the first indicator to the transport chapter tracking annual bus
ridership from 2015-2024.

## Changes
- Added bus ridership indicator section
- Created line chart showing ridership trends
- Calculated percentage change over period
- Added data source citation

## Data Sources
- Bus ridership data: Local Transport Authority annual reports (2015-2024)

## Checklist
- [x] Code runs without errors
- [x] Charts have titles, labels, sources
- [x] Data sources documented
- [x] Code is commented
- [x] Renders successfully
```

**Step 4: Request Review**

- Assign a reviewer (instructor or peer)
- Add label (e.g., "transport", "in-progress")

**Step 5: Submit**
Click "Create pull request"

**BREAK (15 min)**

**Reviewing a Pull Request:**

**As a Reviewer:**

1. Go to "Pull Requests" tab on GitHub
2. Click on a PR to review
3. Click "Files changed" tab
4. Review the changes:
   - Code quality (comments, clarity)
   - Chart labels and formatting
   - Data source documentation
   - Markdown formatting
5. Leave comments:
   - Click line number to comment on specific lines
   - Use "Start a review" to batch comments
6. Submit review:
   - **Approve** - ready to merge
   - **Request changes** - needs fixes
   - **Comment** - suggestions without blocking

**Guided Practice (40 min):**

**Part A: Create PRs (20 min)**
Each analyst creates a pull request for their branch:

1. Ensure branch is pushed to GitHub
2. Go to GitHub and create PR
3. Fill in template with description of their indicator
4. Assign instructor (or peer) as reviewer

**Part B: Peer Review (20 min)**
In pairs, analysts review each other's PRs:

1. Read the description
2. Review the code changes on GitHub
3. Leave at least one constructive comment
4. Approve the PR (if ready) or request changes

**Instructor:** Circulate and provide feedback on both the PRs themselves and the review comments.

### Part 5: Merging and Updating (30 min)

**Merging a Pull Request:**

Once approved:

1. Click "Merge pull request" on GitHub
2. Confirm the merge
3. Delete the branch (GitHub prompts you)

**Locally, update your main branch:**

```bash
# Switch to main
git checkout main

# Pull the latest changes (includes the merged PR)
git pull

# Delete your local feature branch (now merged)
git branch -d yourname/chapter-name

# Verify
git branch
```

**Starting New Work:**

```bash
# Always start from updated main
git checkout main
git pull

# Create new branch for next feature
git checkout -b yourname/next-feature
```

**Guided Practice (15 min):**

1. Instructor merges one example PR (live demo)
2. All analysts pull the latest main branch
3. Verify the merged changes appear in their local main branch
4. Practice creating a new branch from updated main

### Part 6: Merge Conflicts (Basic) (30 min)

**What is a Merge Conflict?**
Occurs when two people edit the same lines of the same file. Git can't auto-merge.

**Scenario Demo:**
Two analysts both edit the same section of a chapter differently.

**Conflict Markers:**

```markdown
## Key Findings

<<<<<<< HEAD
Bus ridership increased by 15% over the period.
=======
Bus ridership showed steady growth, increasing by 12% overall.
>>>>>>> yourname/transport
```

**Resolution Process:**

1. **Identify the conflict** (Git tells you which file)
2. **Open the file** in Positron
3. **Review both versions** (between `<<<<<<<` and `>>>>>>>`)
4. **Choose or combine** the changes
5. **Remove conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`)
6. **Save the file**
7. **Stage and commit:**

   ```bash
   git add chapters/02-transport/index.qmd
   git commit -m "Resolve merge conflict in transport findings"
   git push
   ```

**Live Demonstration:**
Instructor creates and resolves a simple merge conflict.

**Practice (15 min):**
Provide a sample file with conflict markers. Analysts practice resolving it.

**Prevention Tips:**

- Communicate with team about who's working on what
- Pull often to stay updated
- Work on different sections of files when possible
- Keep commits small and focused

### Part 7: WECA Project Git Workflow (20 min)

**Standard Workflow Summary:**

```bash
# 1. Start from main, get latest
git checkout main
git pull

# 2. Create feature branch
git checkout -b yourname/feature-name

# 3. Do your work (edit files)

# 4. Stage and commit often
git add file1.qmd file2.R
git commit -m "Clear, descriptive message"

# 5. Push branch to GitHub
git push -u origin yourname/feature-name

# 6. Create Pull Request on GitHub

# 7. Respond to review comments
git add updated-file.qmd
git commit -m "Address review feedback"
git push  # Updates the PR automatically

# 8. After PR merged, update main
git checkout main
git pull
git branch -d yourname/feature-name
```

**Commit Message Best Practices:**

✅ Good:

```
Add bus ridership indicator to transport chapter
Fix data loading error in helpers.R
Update WECA color palette for accessibility
```

❌ Bad:

```
Updates
Fixed stuff
WIP
asdfasdf
```

**Format:** Imperative mood (like giving a command)

- "Add feature" not "Added feature"
- "Fix bug" not "Fixed bug"

**Pre-Commit Hook Reminder:**
The project has a pre-commit hook that scans for secrets (API keys, passwords). If triggered:

1. Don't bypass it with `--no-verify`
2. Remove the secret from your code
3. Move it to environment variables
4. Try committing again

### Part 8: Final Practice - Full Workflow (45 min)

**Capstone Exercise:**

Each analyst completes the full Git workflow end-to-end:

1. **Update main branch**

   ```bash
   git checkout main
   git pull
   ```

2. **Create a new branch** for a new indicator

   ```bash
   git checkout -b yourname/indicator-2
   ```

3. **Add a second indicator to your chapter:**
   - Copy the structure from your first indicator
   - Use a different dataset or subset
   - Create a different visualization type
   - Write findings narrative

4. **Commit changes** (remember the freeze files!)

   ```bash
   git add chapters/XX-topic/index.qmd
   git add _freeze/html/chapters/XX-topic/
   git commit -m "Add [indicator name] to [chapter] chapter"
   ```

5. **Push branch**

   ```bash
   git push -u origin yourname/indicator-2
   ```

6. **Create Pull Request on GitHub**
   - Fill in template
   - Request peer review

7. **Review a peer's PR**
   - Leave at least 2 comments
   - Approve if ready

**Success Criteria:**

- Branch created and pushed
- PR created with complete description
- Peer review completed
- Ready to merge (don't merge yet - save for instructor)

**Instructor:** This exercise brings together everything from all 5 sessions. Expect questions spanning R, Quarto, file paths, and Git. Provide individualized support.

### Part 9: Course Wrap-up (30 min)

**What We've Accomplished:**

Over 5 sessions, you've learned to:

- ✅ Navigate the command line with Git Bash
- ✅ Use Positron IDE for R development
- ✅ Write R code using tidyverse for data manipulation
- ✅ Create publication-quality visualizations with ggplot2
- ✅ Author reproducible reports with Quarto
- ✅ Use Git and GitHub for version control and collaboration
- ✅ Follow the WECA indicators project workflow

**You can now independently:**

- Import and clean messy datasets
- Create multiple indicators with charts and tables
- Author professional reports combining code and narrative
- Collaborate on the indicators project using branches and PRs

**Next Steps:**

1. **Continue building indicators** for your assigned priority areas
2. **Ask for help** in team chat or via PR reviews
3. **Reference documentation:**
   - GETTING_STARTED.md (setup reminders)
   - CONTRIBUTING.md (workflow details)
   - R helper function documentation (`?load_csv`, etc.)
4. **Practice regularly** - coding skills improve with use

**Resources for Continued Learning:**

- **R for Data Science** (free online book)
- **ggplot2 documentation** and cheat sheet
- **Quarto documentation**
- **Git cheat sheet**
- **Internal team chat** for questions

**Feedback Session (15 min):**

- What worked well in the course?
- What was most challenging?
- What additional support would be helpful?
- Suggestions for future training?

**Q&A (15 min):**
Open floor for any remaining questions.

---

## Homework After Session 5

**Goal:** Build momentum and independence

**Week 1-2 After Course:**

1. **Complete 2 more indicators** in your assigned chapter
2. **Create pull requests** for each indicator
3. **Review 2 PRs** from colleagues
4. **Document any issues** you encounter in team chat

**Ongoing:**

- Regular indicator development following the workflow
- Participation in code reviews
- Sharing tips and helper functions with the team

---

## Instructor Materials Checklist

**Before Each Session:**

- [ ] Test all code examples in Positron
- [ ] Verify example datasets are available
- [ ] Prepare practice branches (Session 1)
- [ ] Create sample conflict scenarios (Session 5)
- [ ] Print reference materials (keyboard shortcuts, Git commands)
- [ ] Test rendering on analyst machines (first session only)

**During Sessions:**

- [ ] Dual screen setup (one for live coding, one for reference materials)
- [ ] Git Bash open for command demonstrations
- [ ] Positron IDE open for coding demonstrations
- [ ] GitHub page ready for PR demonstrations
- [ ] Whiteboard/flip chart for conceptual diagrams

**Materials to Provide:**

- [ ] Printed Git command cheat sheet
- [ ] Printed R tidyverse cheat sheet
- [ ] Printed Markdown syntax reference
- [ ] USB drives with backup example datasets
- [ ] Links to online resources (R4DS, Quarto docs)

---

## Assessment Strategy

**Formative Assessment (During Sessions):**

- Live coding participation
- Pair programming discussions
- Homework completion
- Questions asked (indicator of engagement)

**Summative Assessment (End of Course):**

**Minimum Viable Outcome:**
Each analyst can independently:

1. Import a CSV dataset
2. Clean and transform the data
3. Create a chart with WECA branding
4. Author a complete indicator section in Quarto
5. Render the chapter without errors
6. Create a pull request following the workflow

**Success Rubric:**

| Criterion | Developing | Proficient | Advanced |
|-----------|-----------|-----------|----------|
| **R Code** | Runs with errors, unclear logic | Runs correctly, commented | Efficient, reusable, well-documented |
| **Visualization** | Basic chart, missing labels | Complete chart, WECA theme | Multiple coordinated charts, publication-ready |
| **Quarto** | Renders with warnings, minimal formatting | Clean render, proper structure | Advanced features (cross-refs, tables), polished |
| **Git Workflow** | Needs help with branches/PRs | Follows workflow independently | Helps others, reviews PRs effectively |
| **Documentation** | Minimal or unclear | Data sources cited, findings clear | Comprehensive narrative, inline R code |

**Post-Course Support:**

- Office hours (1 hour/week for 4 weeks)
- Dedicated team chat channel
- Pair programming sessions available
- Instructor code reviews for first 5 PRs

---

## Troubleshooting Guide for Instructors

**Common Issues & Solutions:**

### R Issues

**"Package not found"**

- Solution: `renv::restore()` in R console
- Prevention: Verify renv setup before Session 1

**"File not found"**

- Cause: Hardcoded paths or wrong working directory
- Solution: Use `here::here()` for all paths
- Check: Run `here::here()` to see project root

**"Object not found"**

- Cause: Code chunks run out of order
- Solution: "Restart R Session" in Positron, then run chunks sequentially

**Rendering errors**

- Check R console for specific error
- Verify all packages loaded
- Test render in clean R session

### Git Issues

**"Permission denied (publickey)"**

- Cause: SSH keys not set up
- Solution: Use HTTPS cloning instead, or set up SSH keys
- Check: `git remote -v` shows HTTPS URLs

**"Merge conflict"**

- Walk through resolution step-by-step
- Use Positron's merge conflict UI if available
- Have example conflict file prepared

**"Your branch is behind origin/main"**

- Solution: `git pull` before creating new branch
- Prevention: Always start from updated main

**Can't push (rejected)**

- Cause: Remote has commits not in local
- Solution: `git pull` first, then `git push`

### Quarto Issues

**"Kernel error"**

- Cause: Python/R kernel not found
- Solution: Verify R/Python installation, restart Positron

**"LaTeX error" (PDF rendering)**

- Cause: Missing LaTeX installation
- Solution: Install TinyTeX: `quarto install tinytex`
- Alternative: Focus on HTML output (PDF optional)

**Freeze cache issues**

- If cache gets corrupted: Delete `_freeze/` for that chapter, re-render
- If merge conflicts in freeze: Delete local cache, pull, re-render

### Positron Issues

**Code chunks don't execute**

- Check R session is active (bottom right corner)
- Try "Restart R Session"
- Verify renv activated (look for renv in session info)

**File doesn't open**

- Check file path is correct
- Try reopening project: File > Open Project

---

## Adaptation Notes

**If Time is Short:**

- Sessions 2 and 3 could be combined (8 hours on R)
- Reduce homework review time (move to asynchronous Slack thread)
- Use more instructor demos, less individual practice

**If Analysts Have Some Experience:**

- Start at Session 2 (skip "Whole Game", they do basic setup as homework)
- Add advanced topics: `purrr` for iteration, `targets` for pipelines
- More focus on optimization and code efficiency

**For Remote Delivery:**

- Use breakout rooms for pair programming
- Screen sharing for live coding demos
- Use Slack/Teams chat for async troubleshooting
- Record sessions for reference
- Longer breaks (screen fatigue)

**For Mixed Skill Levels:**

- Pair experienced with beginners
- Provide stretch goals for faster learners
- Differentiated homework (basic + optional challenges)
- Office hours for extra support

---

## Learning Science Principles Applied

This course design incorporates evidence-based teaching methods:

1. **Cognitive Load Management**
   - "Whole Game" first reduces extraneous load (see the forest before the trees)
   - Consistent patterns (load → transform → visualize) reduce cognitive overhead
   - Helper functions reduce syntax complexity
   - Spaced practice via homework spreads learning over time

2. **Active Learning**
   - Live coding with immediate practice (not passive lectures)
   - Minimal lecture time (< 30% of each session)
   - Real-world application from Session 1

3. **Scaffolding**
   - Pre-installed software eliminates setup friction
   - Helper functions abstract complexity initially
   - Example datasets are clean initially, messier in later sessions
   - Gradual release: instructor demo → guided practice → independent work

4. **Social Learning**
   - Pair programming options
   - Peer code review in Session 5
   - Collaborative project (shared indicators repository)

5. **Metacognition**
   - Reflection time in each session wrap-up
   - Debugging strategy explicitly taught
   - Error messages explained (not feared)

6. **Transfer of Learning**
   - All practice uses real WECA data/project structure
   - No toy examples after Session 1
   - Authentic task design (they build actual deliverables)

---

## Success Metrics

**Short-term (End of Course):**

- 100% of analysts complete at least one indicator independently
- 80%+ create PRs following the workflow
- 100% can render a chapter without instructor help

**Medium-term (1 month post-course):**

- Each analyst has contributed 3+ indicators
- PRs are created without prompting
- Analysts help each other in team chat

**Long-term (3 months post-course):**

- Indicators project workflow is self-sustaining
- Analysts propose and implement workflow improvements
- Code quality improves (evidenced by PR reviews)

---

## Conclusion

This 5-session course uses pedagogical best practices to minimize friction and maximize learning for analysts transitioning from Excel to code-first analysis. By combining the "whole game first" approach with active learning, real-world application, and collaborative workflows, analysts will gain both technical skills and confidence in R, Quarto, and Git.

The course design prioritizes practical competence over comprehensive coverage - analysts will be able to *do* the work of creating indicators, with resources available to deepen knowledge as needed. This pragmatic approach respects their time and focuses on achieving the project goal: a sustainable, collaborative, code-first indicators workflow.
