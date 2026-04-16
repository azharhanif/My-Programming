# Project 5 – Microscopy Cell Growth & Culture Tracker –  Solution Guide

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
