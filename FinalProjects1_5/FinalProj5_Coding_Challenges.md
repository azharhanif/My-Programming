# Post-Submission Challenges 

## Phase 1 
Count how many rows have `Viability_pct > 85`.

### solution
```python
def count_high_viability(values):
    total = 0
    for v in values:
        if v > 85:
            total += 1
    return total
```

## Phase 2 
Add a summary column `Count_Gap = final_count - first_count`.

###  solution
```python
summary_df["Count_Gap"] = summary_df["Final_Cell_Count"] - summary_df["First_Cell_Count"]
```

## Phase 3 
Filter rows where `Cell_Count > mean_count` and `Viability_pct < mean_viability`.

### solution
```python
mc = df["Cell_Count"].mean()
mv = df["Viability_pct"].mean()
filtered = df[(df["Cell_Count"] > mc) & (df["Viability_pct"] < mv)]
print(filtered)
```
