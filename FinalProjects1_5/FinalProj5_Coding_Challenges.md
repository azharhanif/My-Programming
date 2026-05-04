# Coding Challenges (Sample)

## Phase 1 
Add a function that counts how many brightness values are below `0.99`.

### solution
```python
def count_low_brightness(values):
    total = 0
    for v in values:
        if v < 0.99:
            total += 1
    return total
```

## Phase 2 
Add a summary column `Brightness_Range = max_brightness - min_brightness`.

### solution
```python
summary_df["Brightness_Range"] = summary_df["Max_Brightness"] - summary_df["Min_Brightness"]
```

## Phase 3 
Filter rows where `Relative_Brightness < sample_mean` and `Time_hr` is between 10 and 20.

### solution
```python
m = df["Relative_Brightness"].mean()
filtered = df[(df["Relative_Brightness"] < m) & (df["Time_hr"] >= 10) & (df["Time_hr"] <= 20)]
print(filtered)
```
