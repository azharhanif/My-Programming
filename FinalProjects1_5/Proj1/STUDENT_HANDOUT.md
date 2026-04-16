# Project 1 – Radiation Decay & Half-Life Analysis Suite

## Background
Radioactive decay appears in nuclear physics, medical imaging, and environmental science.
Teams analyze simulated radiation count data and estimate half-life from repeated measurements.

## Core Task Overview
The team will:
- load radiation count data from CSV files
- clean and organize time/count values
- estimate half-life
- compare trials
- build plots and summary tables
- export final files for reporting

## Team Structure
Recommended 4-student team roles:
- **Student 1** – file loading and validation
- **Student 2** – half-life calculations and fitted values
- **Student 3** – plotting and CSV exports
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
- load one or more decay CSV files
- validate numeric columns
- sort by time if necessary
- plot counts vs time
- compute initial count, minimum count, mean count, and estimated half-life using first-half method
- export `phase1_summary.csv`

### Required outputs
- `raw_decay_plot.png`
- `phase1_summary.csv`
- `phase1_reflection.md`

## Phase 2 – Hard Extension
- compare at least 3 decay trials
- estimate half-life for each trial
- calculate total percent drop from first to last reading
- rank trials by estimated half-life
- create a comparison bar chart

### Student-ID-based module
- **Variant A (0–3):** add background-count correction before computing half-life
- **Variant B (4–6):** compute rolling-average smoothed counts
- **Variant C (7–9):** detect and list unusually high or low points using threshold differences

### Required outputs
- `phase2_summary.csv`
- `half_life_comparison.png`
- `phase2_notes.md`

## Phase 3 – Hard Final Extension
- batch-process all trial files automatically from the `data/` folder
- create a 4-panel dashboard
- build a cleaned combined dataset
- export a final report identifying the most stable trial and the least stable trial
- create one additional summary visualization

### Student-ID-based module
- **Variant A (0–3):** compare raw half-life and corrected half-life side by side
- **Variant B (4–6):** compute residual difference between raw counts and smoothed counts
- **Variant C (7–9):** produce an anomaly report for irregular late-time jumps

### Required outputs
- `combined_decay_data.csv`
- `decay_dashboard.png`
- `phase3_report.txt`

## Minimum Visualization Requirements
- counts vs time
- trial comparison chart
- smoothed vs raw curve
- dashboard summary panel

## Sample Input Files Included
- `data/decay_lab_A.csv`
- `data/decay_lab_B.csv`
- `data/decay_lab_C.csv`

## Folder Layout
```text
project_01_radiation_decay_half_life_analysis_suite/
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