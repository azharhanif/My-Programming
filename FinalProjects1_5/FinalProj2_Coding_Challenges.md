# Coding Challenges (practice, no need to submit)

## Phase 1  
Add a function that counts how many recorded points have `Y_m > 5`.

### solution
```python
def count_high_points(y_values):
    total = 0
    for y in y_values:
        if y > 5:
            total += 1
    return total
```

## Phase 2 
Add a summary column `Height_Range = max_height - min_height` for each trial.

### solution
```python
summary_df["Height_Range"] = summary_df["Max_Height_m"] - summary_df["Min_Height_m"]
```

## Phase 3 
Filter the detailed projectile DataFrame to rows where `X_m > mean_x` and `Y_m < mean_y`.

### solution
```python
mx = df["X_m"].mean()
my = df["Y_m"].mean()
filtered = df[(df["X_m"] > mx) & (df["Y_m"] < my)]
print(filtered)
```
