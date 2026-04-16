# Project 3 – Astronomy Light Curve & Transit Data Explorer

## Background
Astronomy datasets often come in the form of time-series light curves.
Teams inspect star brightness over time and measure the strongest brightness dip regions.

## Core Task Overview
The team will:
- load light-curve CSV files
- clean brightness readings
- compute dip depth and duration estimates
- compare stars
- create plots and summary tables
- export final files for reporting

## Team Structure
Recommended 4-student team roles:
- **Student 1** – data loading and validation
- **Student 2** – dip and duration calculations
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
- load one light-curve CSV file
- validate time and brightness columns
- plot brightness vs time
- identify minimum brightness, average brightness, approximate dip depth, and approximate dip center
- export `phase1_summary.csv`

### Required outputs
- `raw_light_curve.png`
- `phase1_summary.csv`
- `phase1_reflection.md`

## Phase 2 – Hard Extension
- compare at least 3 stars
- compute minimum brightness, dip depth, and approximate dip center for each
- sort stars by dip depth
- create a comparison chart
- add a rolling-average smoothed curve

### Student-ID-based module
- **Variant A (0–3):** compute transit duration using a brightness threshold
- **Variant B (4–6):** normalize brightness values before comparison
- **Variant C (7–9):** remove one-step outliers using neighbour comparison

### Required outputs
- `phase2_summary.csv`
- `dip_depth_comparison.png`
- `phase2_notes.md`

## Phase 3 – Hard Final Extension
- batch-process all star files from `data/`
- create a dashboard comparing stars
- build a cleaned combined dataset
- export a final report identifying the deepest dip and the smoothest dataset
- add one extra plot focused on selected dip regions

### Student-ID-based module
- **Variant A (0–3):** compare raw and normalized dip depth side by side
- **Variant B (4–6):** compute time intervals between low-brightness points
- **Variant C (7–9):** generate an anomaly report for flare-like spikes above baseline

### Required outputs
- `combined_light_curve_data.csv`
- `light_curve_dashboard.png`
- `phase3_report.txt`

## Minimum Visualization Requirements
- raw brightness curve
- smoothed brightness curve
- dip-depth comparison chart
- dashboard summary panel

## Sample Input Files Included
- `data/light_curve_star_A.csv`
- `data/light_curve_star_B.csv`
- `data/light_curve_star_C.csv`

## Folder Layout
```text
project_03_astronomy_light_curve_transit_data_explorer/
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