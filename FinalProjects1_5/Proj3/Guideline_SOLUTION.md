# Project 3 – Astronomy Light Curve & Transit Data Explorer –  Solution Guide

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
