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