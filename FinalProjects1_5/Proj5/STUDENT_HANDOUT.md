# Project 5 – Microscopy Cell Growth & Culture Tracker

## Background
Cell culture and microscopy data appear in biology, biotechnology, and medical lab environments.
Teams analyze cell growth, viability, and size over time.

## Core Task Overview
The team will:
- load culture CSV files
- track cell count, viability, and size
- compare cultures
- create plots and tables
- export final files for reporting

## Team Structure
Recommended 4-student team roles:
- **Student 1** – data loading and validation
- **Student 2** – growth and viability calculations
- **Student 3** – plotting and exports
- **Student 4** – comparison summary and presentation

## Student-ID Module Rule for Phase 2 and Phase 3
Each team has **4 students**. In both Phase 2 and Phase 3, every student implements one extra module based on the last digit of that student's ID:
- **0–3** → Variant A
- **4–6** → Variant B
- **7–9** → Variant C
A team may therefore submit a mix of A/B/C variants in the same phase.

## Serial Evaluation Structure
This project is evaluated in sequence:
1. **Phase 1 must work first**
2. **Phase 2 must extend the Phase 1 code**
3. **Phase 3 must extend the Phase 2 code**

Students are not allowed to discard earlier work and rebuild a separate program for later phases.

## Phase 1 – Easy and Detailed Core Build
- load one culture CSV file
- validate hour, cell count, viability, and size columns
- compute average cell count, average viability, average size, and final cell count
- plot cell count and viability over time
- export `phase1_summary.csv`

### Required outputs
- `cell_count_plot.png`
- `viability_plot.png`
- `phase1_summary.csv`
- `phase1_reflection.md`

## Phase 2 – Hard Extension
- compare at least 3 culture runs
- compute final cell count, average viability, and mean size for each run
- sort runs by final cell count
- create comparison charts
- calculate step-by-step growth ratios

### Student-ID-based module
- **Variant A (0–3):** compute rolling-average growth ratios
- **Variant B (4–6):** detect the first major viability drop
- **Variant C (7–9):** flag unusual size jumps between consecutive rows

### Required outputs
- `phase2_summary.csv`
- `cell_count_comparison.png`
- `phase2_notes.md`

## Phase 3 – Hard Final Extension
- batch-process all culture files from `data/`
- create a dashboard comparing cultures
- build a cleaned combined dataset
- export a final report identifying strongest growth and best viability retention
- add one extra plot for growth ratio or size trend

### Student-ID-based module
- **Variant A (0–3):** compute predicted next-step count using last two steps
- **Variant B (4–6):** recommend a harvest window based on viability and count trends
- **Variant C (7–9):** produce an anomaly report for suspicious drops or jumps

### Required outputs
- `combined_culture_data.csv`
- `culture_dashboard.png`
- `phase3_report.txt`

## Minimum Visualization Requirements
- cell count over time
- viability over time
- average size over time
- culture comparison chart

## Sample Input Files Included
- `data/culture_day_A.csv`
- `data/culture_day_B.csv`
- `data/culture_day_C.csv`

## Folder Layout
```text
project_05_microscopy_cell_growth_culture_tracker/
├── STUDENT_HANDOUT.md
├── TEACHER_SOLUTION.md
├── POST_SUBMISSION_CHALLENGES_SET_A.md
├── POST_SUBMISSION_CHALLENGES_SET_B.md
├── post_submission_challenge_generator_setA.py
├── post_submission_challenge_generator_setB.py
├── starter.py
├── team_solution.py
├── teacher_reference_solution.py
├── data/
├── outputs/
└── README.md
```

## Deliverables
Your GitHub-ready submission folder must include:
- `starter.py`
- `team_solution.py`
- all required plots
- required CSV exports
- a short presentation (`pdf` or `pptx`)
- a `README.md`

## Suggested Rubric (40 marks)
### A. Phase 1 – Core Build (14)
- data loading and validation (4)
- baseline calculations (4)
- required outputs (4)
- readability and modularity (2)

### B. Phase 2 – Extension + Student-ID Modules (13)
- extension of Phase 1 design (3)
- advanced calculations or comparisons (4)
- student-ID module (3)
- output quality (3)

### C. Phase 3 – Final Extension + Student-ID Modules (13)
- extension of earlier phases (3)
- richer outputs or summaries (4)
- student-ID module (3)
- final report quality (3)