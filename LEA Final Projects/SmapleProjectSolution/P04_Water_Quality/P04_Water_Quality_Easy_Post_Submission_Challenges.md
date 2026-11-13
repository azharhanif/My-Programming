# P04 — Water Quality Project
## Three Short Post-Submission Challenges

These challenges are small extensions of the original `project.py`. They use the same dataset, cleaned DataFrame, health-score calculation, and per-site summary already created by the project.

**Instructions:** Complete the challenges in order. Do not rewrite the original project. Add the required code to your existing program or run the supplied instructor solution file from the `P04_Water_Quality` folder.

---

### Phase 1 — Find the highest nitrate reading

**Challenge:** After cleaning the data, find and display the single sample with the highest `Nitrate_mg_L`. Display its `SiteID`, `Date`, and `Nitrate_mg_L`.

**Tricky part:** Use the cleaned DataFrame. Do not search the original uncleaned CSV.

### Phase 2 — Find the site with the highest average nitrate

**Challenge:** After calculating the per-site summary, display the site with the highest `Mean_Nitrate`.

**Tricky part:** Compare site averages, not individual readings. Display the site ID and its average nitrate value.

### Phase 3 — Create a bar chart of average nitrate by site

**Challenge:** Use the existing per-site summary to create a bar chart showing `Mean_Nitrate` for each `SiteID`.

Your chart must include:
- A clear title
- An x-axis label (`Site ID`)
- A y-axis label (`Mean nitrate (mg/L)`)

**Tricky part:** Use the grouped summary from Phase 2. Do not calculate the averages again from the raw data.

---

## Running the instructor solution

1. Keep `challenge_solutions.py` in the same folder as the original `project.py`.
2. Make sure the original `data/water_samples.csv` file is in the `data` folder.
3. Run:

```bash
python challenge_solutions.py
```

The Phase 3 bar chart is saved as `outputs/phase3_mean_nitrate_by_site.png`.
