# Project 1 – Radiation Decay & Half-Life Analysis Suite –  Solution Guide

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
