# Project 1 – Radiation Decay & Half-Life Analysis Suite –  Project Solution Guide

Suggested functions:
- `load_data(paths)`
- `clean_decay(df)`
- `estimate_half_life_simple(df)`
- `background_correct(df, background=5)`
- `smooth_counts(df, window=3)`
- `find_irregular_points(df)`

### Phase 1
- load CSV
- sort by time
- compute initial, minimum, mean counts
- estimate half-life using first time count <= initial/2
- create basic plot

### Phase 2
- compare 3 trials
- compute total percent drop and estimated half-life
- implement one student-ID variant:
  - A: subtract constant background from counts
  - B: rolling-average smoothing
  - C: threshold-based irregular-point detection

### Phase 3
- batch-process files
- combine all outputs
- dashboard and final report
- implement final variant:
  - A: compare raw vs corrected half-life
  - B: residual difference between raw and smoothed counts
  - C: late-time anomaly report


# Project 2 – Projectile Motion Lab Analyzer –  Project Solution Guide

Suggested functions:
- `load_data(paths)`
- `compute_metrics(df)`
- `plot_trajectory(df)`
- `estimate_average_speed(df)`
- `estimate_angle(df)`
- `interpolate_missing_y(df)`
- `path_length(df)`

### Phase 1
- compute max height, range, and flight time
- create x–y plot
- export summary

### Phase 2
- compare trials and sort by range
- add x vs time and y vs time plots
- implement one student-ID variant:
  - A: average horizontal speed
  - B: approximate launch angle from early points
  - C: interpolate one missing y-value

### Phase 3
- batch-process files
- dashboard and combined dataset
- implement final variant:
  - A: path length
  - B: closest point to a target distance
  - C: abrupt vertical-change list


# Project 3 – Astronomy Light Curve & Transit Data Explorer –  Project Solution Guide

Suggested functions:
- `load_data(paths)`
- `smooth_curve(df)`
- `dip_metrics(df)`
- `normalize_curve(df)`
- `remove_outliers(df)`
- `low_brightness_intervals(df, threshold)`

### Phase 1
- compute min brightness, average brightness, dip depth, dip center
- plot raw curve

### Phase 2
- compare 3 stars and sort by dip depth
- add smoothed plot
- implement one student-ID variant:
  - A: threshold-based transit duration
  - B: normalization
  - C: one-step outlier cleanup

### Phase 3
- batch-process files
- dashboard and combined dataset
- implement final variant:
  - A: raw vs normalized dip depth
  - B: low-brightness interval calculation
  - C: flare-spike anomaly report


# Project 4 – Water Quality & Environmental Sensor Monitor –  Project Solution Guide

Suggested functions:
- `load_data(paths)`
- `warning_mask(df)`
- `warning_count(df)`
- `rolling_variable(df, col)`
- `severity_total(df)`
- `fill_missing_value(df, col, idx)`

### Phase 1
- compute basic summaries and warning counts
- plot temperature, pH, dissolved oxygen

### Phase 2
- compare sites and sort by warning count
- implement one student-ID variant:
  - A: rolling average
  - B: severity total
  - C: neighbour-average filling

### Phase 3
- batch-process files
- dashboard and combined dataset
- implement final variant:
  - A: hour-to-hour change
  - B: first warning time
  - C: anomaly list for sudden jumps


# Project 5 – Microscopy Cell Growth & Culture Tracker –  Project Solution Guide

Suggested functions:
- `load_data(paths)`
- `growth_metrics(df)`
- `growth_ratio(df)`
- `rolling_growth(df)`
- `first_major_viability_drop(df)`
- `size_jump_flags(df)`
- `predict_next_count(df)`
- `recommend_harvest_window(df)`

### Phase 1
- compute average cell count, viability, size, and final count
- plot count and viability

### Phase 2
- compare runs and sort by final count
- implement one student-ID variant:
  - A: rolling growth ratio
  - B: first major viability drop
  - C: unusual size jump flags

### Phase 3
- batch-process files
- dashboard and final report
- implement final variant:
  - A: next-step prediction from recent steps
  - B: harvest-window recommendation
  - C: anomaly report for suspicious drops/jumps
