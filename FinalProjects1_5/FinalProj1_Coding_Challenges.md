# Coding Challenges (Sample)

## Phase 1 
Add a function `count_above_threshold(counts, threshold)` that returns how many count values are above a chosen threshold.

### solution
```python
def count_above_threshold(counts, threshold):
    total = 0
    for value in counts:
        if value > threshold:
            total += 1
    return total
```

## Phase 2 
Given a summary table for three trials, add a new column `Count_Range = max_count - min_count`.

### solution
```python
summary_df["Count_Range"] = summary_df["Max_Count"] - summary_df["Min_Count"]
```

## Phase 3 
Filter the detailed DataFrame to rows where `Time_s >= 40` and `Counts` is below the trial average.

### solution
```python
trial_avg = df["Counts"].mean()
filtered = df[(df["Time_s"] >= 40) & (df["Counts"] < trial_avg)]
print(filtered)
```
