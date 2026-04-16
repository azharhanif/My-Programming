# Project 2 – Projectile Motion Lab Analyzer

## Background
Projectile motion connects physics, trigonometry, modelling, and experimentation.
Teams analyze measured position data from launches and compare experimental motion across trials.

## Core Task Overview
The team will:
- load time-position CSV files
- compute trajectory features
- compare multiple launches
- create plots and summary tables
- export results for reporting

## Team Structure
Recommended 4-student team roles:
- **Student 1** – data loading and validation
- **Student 2** – motion calculations
- **Student 3** – plotting and exports
- **Student 4** – summary comparison and presentation

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
- load one projectile CSV file
- validate time, x, and y columns
- compute maximum height, horizontal range, and total flight time
- plot x vs y trajectory
- export `phase1_summary.csv`

### Required outputs
- `trajectory_plot.png`
- `phase1_summary.csv`
- `phase1_reflection.md`

## Phase 2 – Hard Extension
- compare at least 3 launch trials
- compute range, max height, and flight time for each trial
- sort trials by range
- create a comparison table and bar chart
- add x vs time and y vs time plots

### Student-ID-based module
- **Variant A (0–3):** compute average horizontal speed from x/time data
- **Variant B (4–6):** estimate launch angle from early data points
- **Variant C (7–9):** fill one missing y-value by linear interpolation

### Required outputs
- `phase2_summary.csv`
- `range_comparison.png`
- `phase2_notes.md`

## Phase 3 – Hard Final Extension
- automatically process all projectile CSV files from `data/`
- create a dashboard combining key plots
- add a column for step-by-step displacement
- export a final written comparison of the best and weakest trial

### Student-ID-based module
- **Variant A (0–3):** compute total path length using successive points
- **Variant B (4–6):** identify the point closest to a target distance
- **Variant C (7–9):** generate a list of abrupt vertical changes between consecutive points

### Required outputs
- `combined_projectile_data.csv`
- `projectile_dashboard.png`
- `phase3_report.txt`

## Minimum Visualization Requirements
- x–y trajectory
- x vs time
- y vs time
- trial comparison chart

## Sample Input Files Included
- `data/projectile_trial_A.csv`
- `data/projectile_trial_B.csv`
- `data/projectile_trial_C.csv`

## Folder Layout
```text
project_02_projectile_motion_lab_analyzer/
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