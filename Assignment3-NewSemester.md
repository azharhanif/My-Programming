# Programming in Science — Assignment 3
## Data Science, Pandas, NumPy, and Data Visualization

**Total: 100 marks**  
**Code submission: 40 marks**  
**Post-submission challenge: 60 marks**

## Purpose
Use Python to investigate the supplied CSV datasets. Apply the data-science life cycle from OpenStax §15.1: **data acquisition, data exploration, data analysis, and reporting**. Your work will use Pandas DataFrames and Series, NumPy for numerical operations where useful, and Matplotlib for visualization. A graph should help answer a question; an observed relationship does not automatically prove cause and effect.

 
## General requirements
- Read the supplied CSV files in Python; do not manually type dataset values into your program.
- **Pandas is the primary tool for reading and manipulating tabular data.** You must use DataFrames and Series operations.
- **NumPy is permitted and encouraged** for numerical calculations. It is not compulsory to use NumPy in every question.
- Use Matplotlib (`matplotlib.pyplot`) for the required graphs.
- You may use Pandas plotting methods if all graph requirements are met; explicit Matplotlib commands are recommended.
- Do not use Excel or another application to perform the analysis instead of Python. Do not modify the supplied CSV files.
- Every graph needs a meaningful title and labelled axes, including units where appropriate. Save each graph as a PNG using `plt.savefig(...)` before `plt.show()`.
- Organize your program into clearly named functions. Be prepared to explain your code.
### Required tools and concepts

Demonstrate suitable use of `pd.read_csv()`, `head()`, `info()` and/or `describe()`, column selection by label, Series calculations (`mean()`, `max()`, `min()`, `sum()`), Boolean filtering, missing/invalid-value handling, and Matplotlib. You may use NumPy operations such as `np.mean()` and `np.abs()`. You do not need to use every listed function; select appropriate tools for each task.

## Project setup

Create a folder named `Assignment3`, containing `assignment3.py` and a `data` folder. Place all four supplied CSV files in `data`.

```text
Assignment3/
├── assignment3.py
└── data/
    ├── weather_readings.csv
    ├── study_hours_scores.csv
    ├── weekly_sales.csv
    └── sensor_readings_needs_cleaning.csv
```

Install packages if needed:

```bash
python -m pip install pandas numpy matplotlib
```

Run your program from the `Assignment3` folder.

---

# Code Submission — 40 marks

Submit one working Python program named `assignment3.py`. Complete all four tasks.

## Q1 — Read and compare weather measurements (10 marks)

**File:** `data/weather_readings.csv`

Columns: `hour`, `measured_temp_c`, and `model_temp_c`.

Write `analyze_weather(filename)` that:
1. Loads the CSV into a DataFrame using `pd.read_csv()`.
2. Inspects the data using at least one of `head()`, `info()`, or `describe()`.
3. Selects the three required columns by column name.
4. Creates a line graph with measured and model temperatures on the same axes.
5. Includes a title, labelled axes (`Hour of day`, `Temperature (°C)`), legend, and grid.
6. Saves `weather_comparison.png`.

Calculate and print mean absolute error (MAE):

![MAE](MAE.png)


Use NumPy (`np.mean(np.abs(...))`) or an equivalent Pandas/Series calculation. Include °C in the output.

## Q2 — Investigate study hours and quiz scores (10 marks)

**File:** `data/study_hours_scores.csv`

Write `analyze_study_data(filename)` that loads the file into a DataFrame, inspects it, and selects `study_hours` and `quiz_score`. Create a scatter plot with study hours on x and quiz score (%) on y. Add a title, axis labels, and grid. Save `study_hours_vs_score.png`.

Print the number of observations, average quiz score, highest quiz score, and study hours associated with the highest score. Use an appropriate method such as `idxmax()` to find the matching row.

Write 3–4 sentences describing the pattern and one limitation. Explain why this observational dataset does not prove study time alone caused a score.

## Q3 — Compare weekly sales (8 marks)

**File:** `data/weekly_sales.csv`

Write `analyze_sales(filename)` to load the DataFrame, select `day`, `units_sold`, and `revenue_dollars`, and create a bar chart of units sold by day. Include a title and labelled axes; save `weekly_sales.png`. Print total units sold, the day with the highest sales, and the day with the lowest sales. Use Pandas/Series operations and keep day labels correctly associated with their values.

## Q4 — Inspect and clean sensor readings (12 marks)

**File:** `data/sensor_readings_needs_cleaning.csv`

This fictional room-temperature dataset contains a missing value, non-numeric text, and numeric values outside the plausible range for this investigation.

Write `clean_sensor_data(filename)` that:
1. Loads the CSV into a DataFrame.
2. Inspects the temperature column for missing/invalid values.
3. Converts the temperature column to numeric using an appropriate operation; `pd.to_numeric(..., errors="coerce")` is one option.
4. Detects and reports missing values.
5. Detects and reports non-numeric entries.
6. Accepts only numeric temperatures from 0°C to 50°C inclusive.
7. Reports numeric values outside that range.
8. Creates a cleaned DataFrame containing only accepted rows.
9. Plots accepted temperatures against the original reading number, with title, axis labels, markers, and grid.
10. Saves `cleaned_sensor_readings.png`.

Do not silently remove invalid values or overwrite the source CSV. The 0°C–50°C rule is specific to this fictional dataset, not a universal sensor rule.

## Code submission checklist

- [ ] All four files are loaded using Pandas.
- [ ] DataFrames and named columns are used appropriately.
- [ ] Data is inspected and numerical summaries are correct.
- [ ] Missing, non-numeric, and out-of-range sensor values are reported.
- [ ] All four PNG graphs are generated with suitable titles and axis labels.
- [ ] MAE and all requested summary values are printed.
- [ ] Q2 interpretation is included in a separate text file or clearly labelled comment.
- [ ] Code is readable and organized into functions.

## Code marking guide

| Requirement | Marks |
|---|---:|
| Q1: DataFrame loading/inspection, two-series graph, formatting, MAE | 10 |
| Q2: DataFrame/Series use, scatter plot, summaries, interpretation/limitation | 10 |
| Q3: DataFrame loading, bar chart, total and highest/lowest day | 8 |
| Q4: missing/non-numeric/range validation, cleaned DataFrame, line plot | 12 |
| **Total** | **40** |

Equivalent correct Pandas/NumPy approaches receive credit. Marks are for correct reasoning, results, and output—not a single required syntax.


---

# Post-Submission Challenge — 60 marks

The challenge takes place after the code submission. Your instructor will provide changed data, parameters, or a new question. You may use Pandas, NumPy, and Matplotlib. You must explain your decisions and modify your own program.
## Challenge marking guide

| Challenge | Assessment | Marks |
|---|---|---:|
| 1 | Correct selection/filtering, code modification, graph, summary, explanation | 20 |
| 2 | Inspection, missing/invalid handling, cleaning, reporting, explanation | 20 |
| 3 | DataFrame use, analysis, visualization, interpretation, limitation | 20 |
| **Total** | | **60** |
---

## Submission requirements

Submit `assignment3.py`, all four CSV files in the `data` folder, all four generated PNG graphs, and your Q2 interpretation. Zip the complete `Assignment3` folder and submit it through the course submission system. Test the program after extracting the ZIP into a different folder. Do not submit only screenshots.
## Academic expectations

You are responsible for understanding every line of your program. Be prepared to explain DataFrames, Series, column selection, data types, indexing, filtering, missing-value handling, numerical summaries, and plotting. You may consult the lecture notes and OpenStax Chapter 15 while preparing. The post-submission modification must be completed by you.

## References

- Lecture 9: *File I/O — Turning a Program Into a Data Processor*.
- Lecture 10: *Plotting Graphs — From CSV Data to Visual Evidence*.
- Das, U., Lawson, A., Mayfield, C., & Norouzi, N. (2024). *Introduction to Python Programming*. OpenStax, Chapter 15, especially §§15.1–15.5:
  - https://openstax.org/books/introduction-python-programming/pages/15-1-introduction-to-data-science
  - https://openstax.org/books/introduction-python-programming/pages/15-2-numpy
  - https://openstax.org/books/introduction-python-programming/pages/15-3-pandas
  - https://openstax.org/books/introduction-python-programming/pages/15-4-exploratory-data-analysis
  - https://openstax.org/books/introduction-python-programming/pages/15-5-data-visualization
