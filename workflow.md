## Indicator Workflow Overview

This describes the workflow that an analyst goes through to construct an indicator. It's reference material rather than part of the training course.

### Why use Git \ Github?

We're all going to be collaborating on this project so we need a way of tracking version, having a "safe" place to add, change and break code without breaking other people's work. Git enables this.

From the Terminal aka shell (you should see the $ sign). Once you've cloned the repo with `git clone https://github.com/westofengland-ca/weca_regional_indicators.git` you change directory `cd` to the folder with `cd ~/projects/weca_regional_indicators`. You are now in the project folder. In the newly cloned repo you should see `(main)` after your prompt. This means you are on the main branch.

Then you create a new branch and switch into it in one command. For example.
`git checkout -b stevecrawshaw/05-environment`
you should see that your prompt in the terminal now has `(stevecrawshaw/05-environment)` after it. You are now in your own branch and can start to code. Add a new indicator R file, amend one etc.

### Modular Indicator Approach

I've set up the project so that you create \ code a single indicator in a single R file. These will live in the relevant folder e.g. `"C:\Users\steve.crawshaw\projects\weca_regional_indicators\scripts\R\05-environment\RI_5A1_renewable.R"`

A few things to note:

1. Use the name of the indicator as the file name i.e. `RI_5A1_renewable` This helps keep the code traceable and organised.
2. Name the variables you create prefixed by the indicator id. For example a raw dataframe (tibble) variable could be called `RI_5A1_raw_tbl". It's a bit more typing but will help stop conflicts and make the code traceable.
3. This repo has lots of folders and a relatively complex structure. Hence, using the `here` package and function is valuable as it helps you navigate the folders more clearly. `here()` always refers to the project "root", that is the `weca_regional_indicators` folder. So `here("scripts", "R", "05-environment")` will point to this location *no matter where your R script runs from*. The TLDR is **always use here() to refer to a file path in the repo**.

We will cover the learning of R code in the sessions, but essentially the overall process for coding an indicator is:

make sure you're on your branch in git

1. Put your raw data in `data/raw` (this won't get pushed to github - it stays on your machine)
2. Create your R script in Rstudio with file\new\ R script in the scripts/R/05-environment (your chapter) folder
3. load your libraries and source the common R file - see what I have set up in one of my R scripts - like this:
`pacman::p_load(tidyverse, glue, janitor, here) source(here::here("scripts", "R", "_common.R"))`
4. Read your data into a dataframe aka tibble with a function like `RI_5A1_raw_tbl <- read_csv(here::here("data", "raw", "raw_data.csv"))`
5. Transform your data with dplyr verbs - we'll cover this in the sessions
6. Make a chart of your data with ggplot and assign the chart to a plot object called like `RI_51A_plot`
7. Transform your data into a tbl with 3 columns: `period_start, period_end, value` for the time series that you've got - normally <= 10 years.
8. pipe it into the build_fact() and save_fact() functions. These will create standard csv files in `data/fact` that will be used to build the reporting tables for each indicator.
9. add, commit ansd push to git (from the terminal) with e.g.
    `git add scripts/R/05-environment/RI_5A1_renewable.R`
    then
    `git commit -m 'completed RI_5A1_renewable indicator'`
    then push your branch to the repo
    `git push -u origin stevecrawshaw/05-environment`
    we will cover the [git workflow](https://r-quarto-learning.vercel.app/sessions/session-05.html) in the sessions
10. For now, this is it. I will cover how to include the charts and table into the report in another session.
