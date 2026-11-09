# Lab 8 — Exploring Data with Pandas (EDA)


**Estimated time:** 75–90 minutes  
**Topic:** OpenStax §15.4 — Exploratory Data Analysis  
**Preparation for:** Assignment 3

## Learning goals

By the end of this lab, you should be able to:

1. Explain the purpose of exploratory data analysis (EDA).
2. Inspect a DataFrame and access individual entries using `loc[]` and `iloc[]`.
3. Slice and filter a DataFrame to select useful subsets.
4. Identify missing (`Null`/`NaN`) values.
5. Remove or replace missing values and explain the consequences.
6. Create a new feature from existing columns.
7. Use EDA to decide what data is suitable for a later graph or analysis.

## Setup

Create a folder named `Lab8`. Inside it, create `lab8_eda.py` and a folder named `data`. Put both supplied CSV files inside `data`.

```text
Lab8/
├── lab8_eda.py
└── data/
    ├── class_progress.csv
    └── lab_environment.csv
```

Install Pandas if necessary:

```bash
python -m pip install pandas
```

Start your program with:

```python
import pandas as pd

df = pd.read_csv("data/class_progress.csv")
```

Do not use Excel to perform the analysis. Complete the tasks in Python.

---

# Part A — Meet the dataset (10 minutes)

The file `class_progress.csv` contains fictional data for 30 students. It records study hours, practice quiz attempts, attendance, and quiz scores. Some entries are intentionally missing.

### Task A1 — First inspection

Add code to display:

```python
print(df)
print(df.head())
print(df.info())
print(df.describe())
```

Answer in comments or in your lab notes:

1. How many rows and columns are in the dataset?
2. What does one row represent?
3. Which columns contain numerical data?
4. Why is `student_id` not a numerical measurement, even though it contains digits?
5. Which columns have missing values?

### Task A2 — Column selection

Write code to display only:

- `student_id`
- `study_hours`
- `quiz_score`

Then display only the `quiz_score` column.

Hint:

```python
print(df[["student_id", "study_hours", "quiz_score"]])
print(df["quiz_score"])
```

**Check your understanding:** What is the difference between selecting one column as `df["quiz_score"]` and selecting a list of columns as `df[["quiz_score"]]`?

---

# Part B — Indexing with `loc[]` and `iloc[]` (15 minutes)

Pandas supports two common ways to access rows and columns:

- `loc[]`: label-based indexing.
- `iloc[]`: integer-position-based indexing.

### Task B1 — Use `iloc[]`

Write code to display:

1. The first row.
2. The third row.
3. The value in the first row and second column.
4. The first five rows.
5. The first three rows and first two columns.

### Task B2 — Use `loc[]`

Write code to display:

1. The row with index label `4`.
2. The `study_hours` value at index label `4`.
3. Rows with labels 0 through 4, including both endpoints.
4. The `student_id` and `quiz_score` columns for rows with labels 0 through 4.

### Task B3 — Compare

Answer:

1. What does `df.iloc[2]` select?
2. What does `df.loc[2]` select in this DataFrame?
3. Why can `loc[0:4]` include five rows, while ordinary Python slicing `some_list[0:4]` includes four elements?

---

# Part C — Filtering and slicing (15 minutes)

Filtering selects rows that satisfy a condition.

### Task C1 — One condition

Create and display a DataFrame containing only students who studied at least 4 hours.

```python
high_study = df[df["study_hours"] >= 4]
print(high_study)
```

Then answer: How many students meet this condition?

### Task C2 — Multiple conditions

Create and display a DataFrame containing students who:

- studied at least 3 hours; **and**
- achieved a quiz score of at least 75.

Hint: use `&` and put each condition inside parentheses.

```python
selected = df[
    (df["study_hours"] >= 3) &
    (df["quiz_score"] >= 75)
]
```

### Task C3 — Alternative condition

Display students who either studied at least 5 hours **or** achieved a quiz score of at least 90.

Hint: use `|`.

### Task C4 — Sort and inspect

Sort the dataset by `quiz_score` from highest to lowest and display the top five rows.

Hint:

```python
df.sort_values("quiz_score", ascending=False).head()
```

What can you learn from the top five rows? What can you not conclude from them?

---

# Part D — Missing data (20 minutes)

Missing values can affect calculations and conclusions. The dataset contains intentional missing values.

### Task D1 — Identify missing values

Run:

```python
print(df.isnull())
print(df.isnull().sum())
```

Answer:

1. What does `isnull()` return?
2. What does `df.isnull().sum()` calculate?
3. Which columns contain missing values?
4. How many values are missing in each affected column?

### Task D2 — Find incomplete records

Display only rows that contain at least one missing value.

Hint:

```python
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)
```

How many student records are incomplete?

### Task D3 — Remove missing records

Create a new DataFrame that removes rows containing missing values:

```python
complete_df = df.dropna()
```

Print the number of rows before and after removal.

**Think:** What information is lost when incomplete records are removed? Could this create a biased dataset?

### Task D4 — Replace missing values

Create another copy of the original DataFrame. Replace missing `study_hours` values with the mean of the available study-hour values. Replace missing `attendance_percent` values with the mean attendance.

```python
filled_df = df.copy()

filled_df["study_hours"] = filled_df["study_hours"].fillna(
    filled_df["study_hours"].mean()
)
```

Repeat the operation for `attendance_percent`.

Print the affected rows before and after replacement.

**Important:** Do not replace the missing `quiz_score` with an invented score. Explain why filling a missing outcome with the class average could misrepresent an individual student's performance.

### Task D5 — Choose a strategy

In your own words, explain when you might:

- remove a row using `dropna()`;
- replace a missing value using `fillna()`;
- leave the value missing and investigate further.

There is no single correct strategy for every dataset. Your decision should depend on what is missing and why it may be missing.

---

# Part E — Create a new feature and prepare for Assignment 3 (10 minutes)

A **feature** is a variable or attribute calculated from existing data.

### Task E1 — Create a study category

Add a new column called `study_category`:

- `"Low"` for fewer than 2 study hours;
- `"Moderate"` for 2 to fewer than 4 study hours;
- `"High"` for 4 or more study hours.

You may use `.loc[]` with Boolean conditions.

Example starting point:

```python
feature_df = df.copy()

feature_df.loc[
    feature_df["study_hours"] < 2,
    "study_category"
] = "Low"
```

Complete the other two categories. Make sure missing study-hour values remain missing rather than being assigned to a category.

### Task E2 — Summarize the feature

Display the number of students in each category.

Hint:

```python
print(feature_df["study_category"].value_counts())
```

### Task E3 — Prepare a graph-ready dataset

Create a DataFrame containing only rows with valid `study_hours` and `quiz_score`. Display the two columns.

Explain why this cleaned subset is suitable for a scatter plot of study hours versus quiz score.

---

# Part F — Apply EDA to a second dataset (10 minutes)

Open `data/lab_environment.csv`.

This file contains weekly room-temperature readings and a sensor status. Some temperatures are missing, including one week marked `MAINTENANCE`.

Complete the following:

1. Load the file into a DataFrame called `environment_df`.
2. Display `head()`, `info()`, and `isnull().sum()`.
3. Display rows where `lab_temperature_c` is missing.
4. Display only rows where `sensor_status` is `"OK"`.
5. Explain why replacing the missing temperature in the `MAINTENANCE` row with the average may be misleading.
6. Create a new DataFrame containing only rows where the sensor status is `"OK"` and the temperature is not missing.

---

## Final reflection

Answer these questions in 4–6 sentences:

1. What is the main purpose of EDA?
2. How do indexing and filtering help you understand a dataset?
3. Why should you investigate missing values before removing or replacing them?
4. How does this lab prepare you for Assignment 3, especially the sensor-data cleaning task?

## Lab 8 completion checklist

- [ ] I inspected a DataFrame using `head()`, `info()`, and `describe()`.
- [ ] I selected columns by name.
- [ ] I used both `loc[]` and `iloc[]`.
- [ ] I filtered rows using one and multiple conditions.
- [ ] I identified missing values using `isnull()`.
- [ ] I used `dropna()` and `fillna()` on separate DataFrame copies.
- [ ] I explained the consequences of removing or replacing missing values.
- [ ] I created a new feature using existing data.
- [ ] I prepared a cleaned subset for a scatter plot.

## Connection to Assignment 3

Assignment 3 asks you to inspect CSV data, identify data-quality issues, clean records, calculate summaries, and create visualizations. The techniques in this lab are directly useful for:

- inspecting the weather, study-score, sales, and sensor DataFrames;
- selecting the columns needed for each graph;
- filtering records;
- identifying missing values;
- deciding which records should be retained;
- preparing a clean DataFrame before plotting.

**Do not assume that every missing value should be replaced by an average.** Your cleaning decision must make sense for the variable and the context.
