# Lab 9: Plotting Graphs — From CSV Data to Visual Evidence

**Tools:** Python, Pandas, NumPy, Matplotlib, and Seaborn  
**Sample files:** The accompanying `data/` folder

## Learning goals

By the end of this extension, you should be able to:

1. Explain where plotting fits into the data-science life cycle.
2. Load a CSV file directly into a Pandas DataFrame.
3. Inspect columns, rows, and data types before plotting.
4. Use Pandas and NumPy to select, clean, and calculate with numerical data.
5. Choose an appropriate line plot, scatter plot, bar chart, histogram, or density plot.
6. Create visualizations with Matplotlib and Seaborn.
7. Add titles, axis labels with units, legends, and readable figure sizes.
8. Identify a data-quality problem and explain how it affects a graph.
9. Write a short interpretation supported by the plotted data.

## 0. Connect this lecture to OpenStax §15.1

OpenStax introduces a four-stage data-science life cycle:

1. **Data acquisition** — obtain or collect data.
2. **Data exploration** — inspect, clean, and visualize the data.
3. **Data analysis** — use the data to generate insights or build a model.
4. **Reporting** — communicate the findings.

This lecture concentrates on the practical bridge between acquisition and exploration:

```text
CSV file → Pandas DataFrame → inspect and clean → choose a plot
         → visualize → interpret → report
```

A graph is not decoration. It is a tool for asking and answering a question about data.

**Important:** A graph can reveal a pattern, but it does not automatically explain why the pattern exists. Distinguish an observation from a conclusion.

## 1. Prepare your Python environment

Install the required libraries:

```bash
python -m pip install pandas numpy matplotlib seaborn
```

### What is Pandas?

Pandas is a Python library for working with structured data. Its main data structure, the **DataFrame**, stores data in rows and named columns, much like a spreadsheet table.

The `read_csv()` function loads a CSV file directly into a DataFrame. Pandas also helps us inspect columns, select data, filter rows, and calculate summaries.

### What is NumPy?

NumPy is a Python library for numerical computing. It provides arrays and functions for performing calculations on many values efficiently.

For example, NumPy can calculate an average or the absolute difference between two sets of measurements.

### What is Seaborn?

Seaborn is a data-visualization library built on top of Matplotlib. It works directly with Pandas DataFrames and provides convenient functions for statistical visualizations.

In this lecture, **one Seaborn visualization is required**: the scatter plot in Activity 3. The KDE density plot in the extension remains optional.

### Import the libraries

Use these imports near the beginning of your Python file:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Where should the data files go?

Keep your Python file and the `data` folder in the same project folder:

```text
Lecture10/
│
├── plotting_practice.py
└── data/
    ├── weather_readings.csv
    ├── study_hours_scores.csv
    ├── weekly_sales.csv
    ├── exam_scores.csv
    └── sensor_readings_needs_cleaning.csv
```

The examples use paths such as `"data/weather_readings.csv"`. In Google Colab, upload the CSV file(s) to the session or mount Google Drive, then adjust the path.

## 2. First task: load and inspect a CSV file with Pandas

A CSV (comma-separated values) file stores tabular data as rows and columns. We will use Pandas to load the file directly into a DataFrame. We will **not** use Python's built-in `csv.reader` in this lecture.

Open `data/weather_readings.csv`. It contains:

- `hour`: time of day, in 24-hour format;
- `measured_temp_c`: measured temperature, in degrees Celsius;
- `model_temp_c`: temperature predicted by a simple model, in degrees Celsius.

### Example 1 — Load the CSV file

```python
import pandas as pd

weather_df = pd.read_csv("data/weather_readings.csv")

print(weather_df)
```

The result is a DataFrame. Pandas uses the first row of the CSV file as the column headings by default.

### Example 2 — Inspect the DataFrame

```python
print(weather_df.head())
print(weather_df.columns)
print(weather_df.info())
print(weather_df.describe())
```

What each command does:

- `head()` displays the first five rows.
- `columns` displays the column names.
- `info()` shows the column data types and non-missing values.
- `describe()` displays numerical summaries such as count, mean, minimum, and maximum.

### Example 3 — Select a column

```python
hours = weather_df["hour"]
measured = weather_df["measured_temp_c"]
model = weather_df["model_temp_c"]

print(hours)
print(measured)
```

Each selected column is a Pandas Series. Pandas and Matplotlib can work with these Series directly; we do not need to build separate Python lists.

### Checkpoint 1

1. What are the column headings in the DataFrame?
2. What data type does Pandas use for each column?
3. What information does `head()` provide?
4. What information does `describe()` provide?
5. Why should we inspect the data before creating a graph?

## 3. Activity 1 — Plot measured temperature over time

**Question:** How did the temperature change during the day?

Use the `weather_df` DataFrame created in Section 2.

### Step A — Predict

Before running the code, predict whether the graph will rise, fall, or both.

### Step B — Create a line plot

```python
plt.plot(weather_df["hour"], weather_df["measured_temp_c"])
plt.title("Measured Temperature During the Day")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.show()
```

A line plot is useful when the x-axis represents an ordered sequence, such as time.

### Step C — Improve the graph

```python
plt.figure(figsize=(8, 5))
plt.plot(
    weather_df["hour"],
    weather_df["measured_temp_c"],
    marker="o",
    label="Measured temperature"
)

plt.title("Measured Temperature During the Day")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.show()
```

- `figsize=(8, 5)` changes the figure dimensions.
- `marker="o"` marks each observation.
- `label` gives the plotted series a name.
- `plt.legend()` displays the labels.
- `plt.grid(True)` adds a grid to help read values.

### Step D — Interpret

Write two sentences answering:

1. At approximately what hour is the temperature highest?
2. Does the temperature increase throughout the entire period?

Do not claim more than the data supports.

## 4. Activity 2 — Compare measurements with a model

**Question:** How closely does the model match the measured temperature?

Plot both DataFrame columns on the same axes.

```python
plt.figure(figsize=(8, 5))

plt.plot(
    weather_df["hour"],
    weather_df["measured_temp_c"],
    marker="o",
    label="Measured"
)

plt.plot(
    weather_df["hour"],
    weather_df["model_temp_c"],
    marker="s",
    linestyle="--",
    label="Model"
)

plt.title("Measured Temperature vs Model Prediction")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
```

### Think like a programmer and a scientist

1. Why do both lines need the same x-values?
2. At which observations do the lines appear closest?
3. Does the graph show that the model is perfect?
4. What calculation could quantify the difference?

### Small extension — Calculate the error at each observation

NumPy can perform the subtraction for every row at once. This is called a vectorized calculation.

```python
errors = (
    weather_df["measured_temp_c"].to_numpy()
    - weather_df["model_temp_c"].to_numpy()
)

print("Errors:", errors)
```

`to_numpy()` converts a Pandas Series into a NumPy array. NumPy then subtracts the arrays element by element.

**Optional:** Calculate the mean absolute error (MAE):

```python
mae = np.mean(np.abs(errors))
print("Mean absolute error:", mae, "°C")
```

- `np.abs()` makes every error non-negative.
- `np.mean()` calculates the average of those absolute errors.

The MAE gives the average size of the prediction error, ignoring whether the model was above or below the measurement.

## 5. Activity 3 — Seaborn scatter plot: are two variables related?

**Required Seaborn activity**

A **scatter plot** is useful when asking whether two numerical variables appear to be related.

Open `data/study_hours_scores.csv`. It contains study hours and quiz scores for a fictional group of students.

### Step A — Load and inspect the file

```python
study_df = pd.read_csv("data/study_hours_scores.csv")

print(study_df.head())
print(study_df.info())
print(study_df.describe())
```

### Step B — Create a scatter plot using Seaborn

```python
plt.figure(figsize=(7, 5))

sns.scatterplot(
    data=study_df,
    x="study_hours",
    y="quiz_score"
)

plt.title("Study Time and Quiz Score")
plt.xlabel("Study time (hours)")
plt.ylabel("Quiz score (%)")
plt.grid(True)
plt.show()
```

Notice that Seaborn receives the DataFrame through `data=study_df`. We identify the columns by their names using `x` and `y`.

### Interpret carefully

1. Does the graph suggest a positive relationship, a negative relationship, or no clear relationship?
2. Are there points that do not follow the general pattern?
3. Can we conclude that studying longer *caused* a higher score?
4. What other factors might affect quiz scores?

**Scientific caution:** A relationship between two variables does not, by itself, prove causation. This is a small fictional dataset, not a controlled experiment.

### Student task

Change the graph title and write a three-sentence interpretation. Include one observation, one limitation, and one question you would investigate next.

## 6. Activity 4 — Bar chart: compare categories

A **bar chart** is useful for comparing values across categories.

Open `data/weekly_sales.csv`. It records the number of units sold on each day.

### Load and inspect the data

```python
sales_df = pd.read_csv("data/weekly_sales.csv")

print(sales_df.head())
print(sales_df.info())
```

### Create the bar chart

```python
plt.figure(figsize=(8, 5))

plt.bar(sales_df["day"], sales_df["units_sold"])

plt.title("Units Sold by Day")
plt.xlabel("Day")
plt.ylabel("Units sold")
plt.show()
```

### Student task

1. Find and print the day with the highest sales.
2. Find and print the day with the lowest sales.
3. Calculate the total units sold during the week.
4. Add a sentence explaining which day had the highest sales.

Use the DataFrame column and NumPy functions:

```python
highest = sales_df["units_sold"].max()
lowest = sales_df["units_sold"].min()
total = np.sum(sales_df["units_sold"])

best_day = sales_df.loc[
    sales_df["units_sold"].idxmax(), "day"
]

worst_day = sales_df.loc[
    sales_df["units_sold"].idxmin(), "day"
]

print("Highest sales:", highest, "on", best_day)
print("Lowest sales:", lowest, "on", worst_day)
print("Total units sold:", total)
```

**Think carefully:** `idxmax()` and `idxmin()` return the index label of the row containing the largest or smallest value. We use `.loc[]` to retrieve the corresponding day.

## 7. Activity 5 — Histogram: understand a distribution

A **histogram** groups numerical observations into intervals (bins). It helps answer questions about the distribution of one numerical variable.

Open `data/exam_scores.csv`.

### Load and inspect the scores

```python
exam_df = pd.read_csv("data/exam_scores.csv")

print(exam_df.head())
print(exam_df.info())
print(exam_df.describe())
```

The original activity reads the first CSV column as the exam score. Select that first column from the DataFrame:

```python
scores = exam_df.iloc[:, 0]

print("Number of scores:", len(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Average:", np.mean(scores))
```

### Create a histogram

```python
plt.figure(figsize=(8, 5))

plt.hist(scores, bins=6, edgecolor="black")

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam score (%)")
plt.ylabel("Number of students")
plt.show()
```

The `bins` argument controls how many intervals are used. Changing the number of bins can change how the distribution appears.

### Investigate

1. Which score interval contains the most observations?
2. Are most scores grouped together or spread out?
3. What information does the histogram show that a list of scores does not show as easily?
4. What might be hidden if we use too few bins? What might happen if we use too many?

## 8. Extension — Density plot (KDE)

A density plot is a smoothed estimate of a numerical distribution. It is related to a histogram, but it does not show counts in discrete bins.


```python
plt.figure(figsize=(8, 5))

sns.kdeplot(data=exam_df, x="score")

plt.title("Estimated Distribution of Exam Scores")
plt.xlabel("Exam score (%)")
plt.ylabel("Estimated density")
plt.show()
```

### Compare the histogram and density plot

1. Which one shows counts in intervals?
2. Which one shows a smoothed estimate?
3. Does the density curve prove that the scores follow a particular theoretical distribution?
4. Why should we be cautious when interpreting a smooth curve based on a small dataset?

**Important:** A KDE curve is an estimate. Its shape depends partly on the smoothing method and bandwidth. It does not create new observations or prove a statistical model.

## 9. Activity 6 — Debug and clean a dataset

Real datasets are not always clean. Open `data/sensor_readings_needs_cleaning.csv`.

The file contains a missing temperature and an implausible value. Do not assume that every value in a CSV is valid.

### Step A — Load and inspect the file

```python
sensor_df = pd.read_csv("data/sensor_readings_needs_cleaning.csv")

print(sensor_df.head())
print(sensor_df.info())
print(sensor_df.isnull().sum())
```

Pandas normally represents a blank numeric cell as `NaN` (Not a Number).

### Step B — Identify the problems

- A missing temperature is represented by `NaN`.
- `999.0` is suspicious for this fictional room-temperature sensor dataset.
- A graph created without checking these values could be misleading.

Display the rows with missing temperatures:

```python
temperature_column = sensor_df.columns[1]
print(sensor_df[sensor_df[temperature_column].isna()])
```

Display the rows containing the suspicious value:

```python
print(sensor_df[sensor_df[temperature_column] == 999.0])
```

### Step C — Create a cleaned DataFrame

For this exercise only, use a simple rule: keep numeric temperatures between 0°C and 50°C. This also removes missing values because `NaN` does not satisfy the comparison.

```python
temperature_column = sensor_df.columns[1]

clean_df = sensor_df.loc[
    (sensor_df[temperature_column] >= 0)
    & (sensor_df[temperature_column] <= 50)
].copy()

print("Original number of rows:", len(sensor_df))
print("Valid observations:", len(clean_df))
```

### Step D — Plot the cleaned data

The original activity uses the first column for the reading number and the second column for temperature. Select them by position so the example does not depend on a renamed header:

```python
plt.figure(figsize=(8, 5))

plt.plot(
    clean_df.iloc[:, 0],
    clean_df.iloc[:, 1],
    marker="o"
)

plt.title("Cleaned Room Temperature Readings")
plt.xlabel("Reading number")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

### Discuss

1. Which values were excluded?
2. Why is `999.0` suspicious in this context?
3. Is the 0°C to 50°C rule universally correct for every temperature dataset?
4. Why should a programmer document a cleaning rule instead of silently deleting data?

**Key idea:** Data-cleaning decisions depend on context. A value that is invalid for one sensor may be valid in another setting.

## 10. Debugging checklist

When a plot does not appear or looks incorrect, check one issue at a time.

### File and data problems

- Is the CSV file in the expected folder?
- Is the file name spelled correctly?
- Are the column headers correct?
- Did Pandas load the columns with appropriate data types?
- Are any values missing? Try `df.isnull().sum()`.
- Are there unexpected or implausible values?

### Plotting problems

- Do the x and y columns contain the same number of rows?
- Is the selected plot appropriate for the question?
- Are the axis labels and units correct?
- Does the graph have a meaningful title?
- Is `plt.show()` reached?
- Does the graph use an appropriate scale?

### Common error: mismatched lengths

```python
x = np.array([1, 2, 3])
y = np.array([10, 20])

if len(x) != len(y):
    print("Error: x and y must have the same number of values.")
else:
    plt.plot(x, y)
    plt.show()
```

### Common error: text values used as numbers

If a numerical column was imported as text, inspect its type:

```python
print(weather_df.dtypes)
```

If necessary, convert the column:

```python
weather_df["measured_temp_c"] = pd.to_numeric(
    weather_df["measured_temp_c"],
    errors="coerce"
)
```

`errors="coerce"` converts values that cannot be interpreted as numbers into `NaN`. Inspect the affected rows before deciding what to do with them.

## 11. Plot selection guide

| Question | Suitable plot |
|---|---|
| How does a measurement change over time? | Line plot |
| Do two numerical variables appear related? | Scatter plot |
| How do categories compare? | Bar chart |
| How are numerical observations distributed across intervals? | Histogram |
| What is a smoothed estimate of a numerical distribution? | Density plot (KDE) |

No plot is automatically best. Choose one based on the question and the structure of the data.

## 12. Final hands-on challenge — Investigate a dataset

Work individually or in pairs. Choose one supplied CSV file that you have not used in a previous activity, or ask your instructor for another dataset.

Your program must:

1. Load the CSV file into a Pandas DataFrame using `pd.read_csv()`.
2. Identify the column names and data types you need.
3. Check for missing or suspicious values.
4. Choose a plot that suits a specific question.
5. Use Matplotlib or Seaborn to create the plot.
6. Use at least one NumPy function for a numerical summary (for example, `np.mean()`, `np.min()`, `np.max()`, or `np.sum()`).
7. Add a meaningful title and axis labels, including units where appropriate.
8. Print the numerical summary.
9. Write a short interpretation of the graph.

### Submit

- Your Python source file (`.py`).
- The CSV file used.
- The graph (saved as an image).
- A short interpretation (3–5 sentences).

To save a graph:

```python
plt.savefig("my_graph.png", dpi=150, bbox_inches="tight")
plt.show()
```

Call `savefig()` before `show()`.

### Reflection questions

1. What question were you trying to answer?
2. Why did you choose this type of graph?
3. What is one pattern you observed?
4. What is one limitation of the dataset or graph?
5. What additional data would help you investigate further?

## 13. Summary

You practiced a small data-science workflow:

```text
Acquire → Load into DataFrame → Inspect → Clean
        → Calculate → Visualize → Interpret → Report
```

You used Pandas to load and inspect CSV data, NumPy to perform numerical calculations, Matplotlib to create common plots, and Seaborn to create a required scatter plot and an optional density plot.

Most importantly, you practiced choosing a graph to answer a question rather than creating a graph simply because a plotting function is available.

**Remember:** A correct graph requires more than correct syntax. The data, units, labels, plot type, and interpretation all matter.

## Reference

Das, U., Lawson, A., Mayfield, C., & Norouzi, N. (2024). *Introduction to Python Programming*. OpenStax. Section 15.1, "Introduction to Data Science."  
https://openstax.org/books/introduction-python-programming/pages/15-1-introduction-to-data-science
