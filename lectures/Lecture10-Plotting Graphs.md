# Lecture 10 Extension: Plotting Graphs --- From CSV Data to Visual Evidence

**Course:** Programming in Science\
**Prerequisite:** OpenStax, *Introduction to Python Programming*, §15.1,
"Introduction to Data Science"\
**Suggested duration:** Two class periods, or one 100--120 minute lab\
**Tools:** Python, its built-in `csv` module, Matplotlib, and optional
Seaborn\
**Sample files:** The accompanying `data/` folder

## Learning goals

By the end of this extension, you should be able to:

1.  Explain where plotting fits into the data-science life cycle.
2.  Read a small CSV dataset into Python.
3.  Inspect data before plotting it.
4.  Convert text read from a CSV file into numeric values.
5.  Choose an appropriate line plot, scatter plot, bar chart, histogram,
    or density plot.
6.  Add titles, axis labels with units, legends, and readable figure
    sizes.
7.  Identify a data-quality problem and explain how it affects a graph.
8.  Write a short interpretation supported by the plotted data.

## 0. Connect this lecture to OpenStax §15.1

OpenStax introduces a four-stage data-science life cycle:

1.  **Data acquisition** --- obtain or collect data.
2.  **Data exploration** --- inspect, clean, and visualize the data.
3.  **Data analysis** --- use the data to generate insights or build a
    model.
4.  **Reporting** --- communicate the findings.

This lecture concentrates on the practical bridge between acquisition
and exploration:

``` text
CSV file → read data → inspect and clean → choose a plot
         → visualize → interpret → report
```

A graph is not decoration. It is a tool for asking and answering a
question about data.

**Important:** A graph can reveal a pattern, but it does not
automatically explain why the pattern exists. Distinguish an observation
from a conclusion.

## 1. Prepare your Python environment

Install Matplotlib:

``` bash
python -m pip install matplotlib
```

For the optional density-plot activity, also install Seaborn:

``` bash
python -m pip install seaborn
```

Import Matplotlib:

``` python
import matplotlib.pyplot as plt
```

### Where should the data files go?

Keep your Python file and the `data` folder in the same project folder:

``` text
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

The examples use paths such as `"data/weather_readings.csv"`. In Google
Colab, upload the CSV file(s) to the session or mount Google Drive, then
adjust the path.

## 2. First task: inspect a CSV file before plotting

A CSV (comma-separated values) file stores tabular data as rows and
columns. Python's built-in `csv` module can read it; we do not need
Pandas for this introductory exercise.

Open `data/weather_readings.csv`. It contains:

-   `hour`: time of day, in 24-hour format;
-   `measured_temp_c`: measured temperature, in degrees Celsius;
-   `model_temp_c`: temperature predicted by a simple model, in degrees
    Celsius.

### Example 1 --- Read the file and inspect its rows

**Predict before running:** What do you expect `reader` to contain? Will
the values be strings or numbers?

``` python
import csv

with open("data/weather_readings.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

`csv.DictReader` uses the first row as column names. Each row is
returned as a dictionary. Values read from a CSV file are strings, even
if they look like numbers.

### Example 2 --- Convert columns to numeric lists

``` python
import csv

hours = []
measured = []
model = []

with open("data/weather_readings.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        hours.append(int(row["hour"]))
        measured.append(float(row["measured_temp_c"]))
        model.append(float(row["model_temp_c"]))

print("Hours:", hours)
print("Measured:", measured)
print("Model:", model)
print("Number of observations:", len(hours))
```

**Why convert?** Plotting and numerical calculations require numeric
values. The string `"18.7"` is not the same data type as the number
`18.7`.

### Checkpoint 1

1.  What are the column names in the CSV file?
2.  Why do we use `int()` for `hour` and `float()` for temperature?
3.  What would happen if we tried to calculate `"18.7" + 2`?
4.  Why should we inspect the data before creating a graph?

## 3. Activity 1 --- Plot measured temperature over time

**Question:** How did the temperature change during the day?

Use the lists created in Example 2.

### Step A --- Predict

Before running the code, predict whether the graph will rise, fall, or
both.

### Step B --- Create a line plot

``` python
import matplotlib.pyplot as plt

plt.plot(hours, measured)
plt.title("Measured Temperature During the Day")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.show()
```

A line plot is useful when the x-axis represents an ordered sequence,
such as time.

### Step C --- Improve the graph

``` python
plt.figure(figsize=(8, 5))
plt.plot(hours, measured, marker="o", label="Measured temperature")

plt.title("Measured Temperature During the Day")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.show()
```

-   `figsize=(8, 5)` changes the figure dimensions.
-   `marker="o"` marks each observation.
-   `label` gives the plotted series a name.
-   `plt.legend()` displays the labels.
-   `plt.grid(True)` adds a grid to help read values.

### Step D --- Interpret

Write two sentences answering:

1.  At approximately what hour is the temperature highest?
2.  Does the temperature increase throughout the entire period?

Do not claim more than the data supports.

## 4. Activity 2 --- Compare measurements with a model

**Question:** How closely does the model match the measured temperature?

Plot both series on the same axes.

``` python
plt.figure(figsize=(8, 5))
plt.plot(hours, measured, marker="o", label="Measured")
plt.plot(hours, model, marker="s", linestyle="--", label="Model")

plt.title("Measured Temperature vs Model Prediction")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
```

### Think like a programmer and a scientist

1.  Why do both lines need the same x-values?
2.  At which observations do the lines appear closest?
3.  Does the graph show that the model is perfect?
4.  What additional calculation could quantify the difference?

### Small extension --- Calculate the error at each observation

``` python
errors = []
for i in range(len(measured)):
    errors.append(measured[i] - model[i])

print("Errors:", errors)
```

**Optional:** Calculate the mean absolute error (MAE):

``` python
total_error = 0
for error in errors:
    total_error += abs(error)

mae = total_error / len(errors)
print("Mean absolute error:", mae, "°C")
```

The MAE gives the average size of the prediction error, ignoring whether
the model was above or below the measurement.

## 5. Activity 3 --- Scatter plot: are two variables related?

A **scatter plot** is useful when asking whether two numerical variables
appear to be related.

Open `data/study_hours_scores.csv`. It contains study hours and quiz
scores for a fictional group of students.

### Read the file

``` python
import csv

study_hours = []
quiz_scores = []

with open("data/study_hours_scores.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        study_hours.append(float(row["study_hours"]))
        quiz_scores.append(float(row["quiz_score"]))

print(study_hours)
print(quiz_scores)
```

### Plot the relationship

``` python
plt.figure(figsize=(7, 5))
plt.scatter(study_hours, quiz_scores)

plt.title("Study Time and Quiz Score")
plt.xlabel("Study time (hours)")
plt.ylabel("Quiz score (%)")
plt.grid(True)
plt.show()
```

### Interpret carefully

1.  Does the graph suggest a positive relationship, a negative
    relationship, or no clear relationship?
2.  Are there points that do not follow the general pattern?
3.  Can we conclude that studying longer *caused* a higher score?
4.  What other factors might affect quiz scores?

**Scientific caution:** A relationship between two variables does not,
by itself, prove causation. This is a small fictional dataset, not a
controlled experiment.

### Student task

Change the graph title and write a three-sentence interpretation.
Include one observation, one limitation, and one question you would
investigate next.

## 6. Activity 4 --- Bar chart: compare categories

A **bar chart** is useful for comparing values across categories.

Open `data/weekly_sales.csv`. It records the number of units sold on
each day.

``` python
import csv

days = []
units_sold = []

with open("data/weekly_sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        days.append(row["day"])
        units_sold.append(int(row["units_sold"]))

plt.figure(figsize=(8, 5))
plt.bar(days, units_sold)
plt.title("Units Sold by Day")
plt.xlabel("Day")
plt.ylabel("Units sold")
plt.show()
```

### Student task

1.  Find and print the day with the highest sales.
2.  Find and print the day with the lowest sales.
3.  Calculate the total units sold during the week.
4.  Add a sentence explaining which day had the highest sales.

Hint:

``` python
largest = max(units_sold)
position = units_sold.index(largest)
best_day = days[position]
```

## 7. Activity 5 --- Histogram: understand a distribution

A **histogram** groups numerical observations into intervals (bins). It
helps answer questions about the distribution of one numerical variable.

Open `data/exam_scores.csv`.

### Read the scores

``` python
import csv

scores = []
with open("data/exam_scores.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores.append(float(row["score"]))

print("Number of scores:", len(scores))
print("Minimum:", min(scores))
print("Maximum:", max(scores))
```

### Create a histogram

``` python
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=6, edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam score (%)")
plt.ylabel("Number of students")
plt.show()
```

The `bins` argument controls how many intervals are used. Changing the
number of bins can change how the distribution appears.

### Investigate

1.  Which score interval contains the most observations?
2.  Are most scores grouped together or spread out?
3.  What information does the histogram show that a list of scores does
    not show as easily?
4.  What might be hidden if we use too few bins? What might happen if we
    use too many?

## 8. Extension --- Density plot (KDE)

A density plot is a smoothed estimate of a numerical distribution. It is
related to a histogram, but it does not show counts in discrete bins.

Install Seaborn if needed:

``` bash
python -m pip install seaborn
```

Then run:

``` python
import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(scores)
plt.title("Estimated Distribution of Exam Scores")
plt.xlabel("Exam score (%)")
plt.ylabel("Estimated density")
plt.show()
```

### Compare the histogram and density plot

1.  Which one shows counts in intervals?
2.  Which one shows a smoothed estimate?
3.  Does the density curve prove that the scores follow a particular
    theoretical distribution?
4.  Why should we be cautious when interpreting a smooth curve based on
    a small dataset?

**Important:** A KDE curve is an estimate. Its shape depends partly on
the smoothing method and bandwidth. It does not create new observations
or prove a statistical model.

## 9. Activity 6 --- Debug and clean a dataset

Real datasets are not always clean. Open
`data/sensor_readings_needs_cleaning.csv`.

The file contains a missing temperature and an implausible value. Do not
assume that every value in a CSV is valid.

### Step A --- Inspect the file

``` python
import csv

readings = []
temperatures = []

with open("data/sensor_readings_needs_cleaning.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        readings.append(int(row["reading"]))
        value = row["temperature_c"]
        if value == "":
            temperatures.append(None)
        else:
            temperatures.append(float(value))

print(readings)
print(temperatures)
```

### Step B --- Identify the problems

-   `None` represents a missing value.
-   `999.0` is suspicious for this fictional room-temperature sensor
    dataset.
-   A graph created without checking these values could be misleading.

### Step C --- Create a cleaned version

For this exercise only, use a simple rule: keep numeric temperatures
between 0°C and 50°C, and skip missing or out-of-range readings.

``` python
clean_readings = []
clean_temperatures = []

for i in range(len(temperatures)):
    value = temperatures[i]
    if value is not None and 0 <= value <= 50:
        clean_readings.append(readings[i])
        clean_temperatures.append(value)

print("Valid observations:", len(clean_temperatures))
```

### Step D --- Plot the cleaned data

``` python
plt.figure(figsize=(8, 5))
plt.plot(clean_readings, clean_temperatures, marker="o")
plt.title("Cleaned Room Temperature Readings")
plt.xlabel("Reading number")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

### Discuss

1.  Which values were excluded?
2.  Why is `999.0` suspicious in this context?
3.  Is the 0°C to 50°C rule universally correct for every temperature
    dataset?
4.  Why should a programmer document a cleaning rule instead of silently
    deleting data?

**Key idea:** Data cleaning decisions depend on context. A value that is
invalid for one sensor may be valid in another setting.

## 10. Debugging checklist

When a plot does not appear or looks incorrect, check one issue at a
time.

### File and data problems

-   Is the CSV file in the expected folder?
-   Is the file name spelled correctly?
-   Are the column headers correct?
-   Did the program convert numeric strings using `int()` or `float()`?
-   Are any values missing?
-   Are there unexpected or implausible values?

### Plotting problems

-   Are the x and y lists the same length?
-   Is the selected plot appropriate for the question?
-   Are the axis labels and units correct?
-   Does the graph have a meaningful title?
-   Is `plt.show()` reached?
-   Does the graph use an appropriate scale?

### Common error: mismatched lengths

``` python
x = [1, 2, 3]
y = [10, 20]
plt.plot(x, y)
```

Check before plotting:

``` python
if len(x) != len(y):
    print("Error: x and y must have the same number of values.")
else:
    plt.plot(x, y)
    plt.show()
```

### Common error: plotting strings

``` python
values = ["12.5", "13.0", "14.2"]
numeric_values = []
for value in values:
    numeric_values.append(float(value))
```

## 11. Plot selection guide

  -----------------------------------------------------------------------
  Question                            Suitable plot
  ----------------------------------- -----------------------------------
  How does a measurement change over  Line plot
  time?                               

  Do two numerical variables appear   Scatter plot
  related?                            

  How do categories compare?          Bar chart

  How are numerical observations      Histogram
  distributed across intervals?       

  What is a smoothed estimate of a    Density plot (KDE)
  numerical distribution?             
  -----------------------------------------------------------------------

No plot is automatically best. Choose one based on the question and the
structure of the data.

## 12. Final hands-on challenge --- Investigate a dataset

Work individually or in pairs. Choose one supplied CSV file that you
have not used in a previous activity, or ask your instructor for another
dataset.

Your program must:

1.  Read the CSV file.
2.  Identify the columns and data types you need.
3.  Check for missing or suspicious values.
4.  Choose a plot that suits a specific question.
5.  Add a meaningful title and axis labels, including units where
    appropriate.
6.  Calculate at least one numerical summary (for example, minimum,
    maximum, average, or total).
7.  Print the summary.
8.  Write a short interpretation of the graph.

### Submit

-   Your Python source file (`.py`).
-   The CSV file used.
-   The graph (saved as an image).
-   A short interpretation (3--5 sentences).

To save a graph:

``` python
plt.savefig("my_graph.png", dpi=150, bbox_inches="tight")
plt.show()
```

Call `savefig()` before `show()`.

### Reflection questions

1.  What question were you trying to answer?
2.  Why did you choose this type of graph?
3.  What is one pattern you observed?
4.  What is one limitation of the dataset or graph?
5.  What additional data would help you investigate further?

## 13. Summary

You practiced a small data-science workflow:

``` text
Acquire → Inspect → Clean → Visualize → Interpret → Report
```

You used CSV files, Python's `csv` module, Matplotlib, and an optional
Seaborn density plot. Most importantly, you practiced choosing a graph
to answer a question rather than creating a graph simply because a
plotting function is available.

**Remember:** A correct graph requires more than correct syntax. The
data, units, labels, plot type, and interpretation all matter.

## Reference

Das, U., Lawson, A., Mayfield, C., & Norouzi, N. (2024). *Introduction
to Python Programming*. OpenStax. Section 15.1, "Introduction to Data
Science."\
https://openstax.org/books/introduction-python-programming/pages/15-1-introduction-to-data-science
