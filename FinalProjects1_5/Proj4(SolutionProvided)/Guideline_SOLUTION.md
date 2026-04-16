# Project 4 – Water Quality & Environmental Sensor Monitor –  Solution Guide

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
