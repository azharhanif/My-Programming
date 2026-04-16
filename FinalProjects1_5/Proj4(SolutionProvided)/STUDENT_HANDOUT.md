# Project 4 – Water Quality & Environmental Sensor Monitor

## Background
Environmental monitoring combines chemistry, data collection, and public-health style reporting.
Teams analyze sensor data from river or lake monitoring stations.

## Core Task Overview
The team will:
- load water sensor CSV files
- inspect temperature, pH, dissolved oxygen, turbidity, and conductivity
- flag unusual readings
- compare sites
- create plots and summary tables

## Team Structure
Recommended 4-student team roles:
- **Student 1** – data loading and validation
- **Student 2** – calculations and threshold analysis
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
- load one sensor CSV file
- validate columns and timestamps
- compute summary statistics
- plot at least 3 variables over time
- count rows outside safe thresholds
- export `phase1_summary.csv`

### Required outputs
- `temp_plot.png`
- `ph_plot.png`
- `oxygen_plot.png`
- `phase1_summary.csv`
- `phase1_reflection.md`

## Phase 2 – Hard Extension
- compare at least 3 monitoring sites
- compute average values for all sensor columns
- count warning rows per site
- create a comparison table and bar chart
- sort sites by warning count

### Student-ID-based module
- **Variant A (0–3):** add rolling averages for one selected variable
- **Variant B (4–6):** compute threshold severity totals for each site
- **Variant C (7–9):** fill one missing sensor value using neighbour averages

### Required outputs
- `phase2_summary.csv`
- `warning_count_comparison.png`
- `phase2_notes.md`

## Phase 3 – Hard Final Extension
- batch-process all site files from `data/`
- create a dashboard summarizing all sites
- build a cleaned combined dataset
- export a final report identifying the best and worst site
- add a plot showing the timeline of warnings

### Student-ID-based module
- **Variant A (0–3):** compute hour-to-hour change for one sensor
- **Variant B (4–6):** find the first time each site enters warning status
- **Variant C (7–9):** produce an anomaly list for sudden jumps

### Required outputs
- `combined_water_data.csv`
- `water_dashboard.png`
- `phase3_report.txt`

## Minimum Visualization Requirements
- temperature trend
- pH trend
- dissolved oxygen trend
- warning count comparison chart

## Sample Input Files Included
- `data/river_site_A.csv`
- `data/river_site_B.csv`
- `data/river_site_C.csv`

## Folder Layout
```text
project_04_water_quality_environmental_sensor_monitor/
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