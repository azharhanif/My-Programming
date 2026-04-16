# Project 2 – Projectile Motion Lab Analyzer –  Solution Guide

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
