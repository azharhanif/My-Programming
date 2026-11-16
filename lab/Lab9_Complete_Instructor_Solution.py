"""
LAB 9 — COMPLETE SOLUTION
Plotting Graphs: Pandas, NumPy, Matplotlib, and Seaborn

This file provides commented solutions for the activities in Lab 9:
  1. Load and inspect weather data with Pandas
  2. Line plot of measured temperature
  3. Compare measured and model temperatures
  4. Calculate prediction errors and MAE with NumPy
  5. Seaborn scatter plot: study hours vs quiz scores
  6. Bar chart: weekly sales + highest/lowest/total
  7. Histogram: exam scores (Matplotlib)
  8. Optional KDE plot of exam scores (Seaborn)
  9. Clean sensor readings and plot valid temperatures
 10. Histogram comparison: Matplotlib vs Seaborn using car_crashes
 11. Seaborn histogram with KDE and comparison by speeding group

HOW TO USE
-----------
1. Put this .py file in your Lab 9 project folder.
2. Put available CSV files in a subfolder named "data".
3. The weather CSV supplied with the lab should be named either:
       data/weather_readings.csv
4. Add the other lab CSV files to the same data folder:
       study_hours_scores.csv
       weekly_sales.csv
       exam_scores.csv
       sensor_readings_needs_cleaning.csv
5. Run:
       python Lab9_Complete_Solution.py

If a dataset other than weather_readings.csv is not present, the program
prints a clear message and continues with the other activities.

Required packages:
    python -m pip install pandas numpy matplotlib seaborn

NOTE ABOUT THE CAR-CRASHES DATA:
Seaborn's load_dataset("car_crashes") may need internet access the first
time it is used. If it cannot download the sample dataset, that section
will be skipped with a message. All other activities use local CSV files.
"""

from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator


# ---------------------------------------------------------------------
# PART 0 — FILE LOCATIONS AND OUTPUT FOLDER
# ---------------------------------------------------------------------

# The script assumes that the "data" folder is beside this Python file.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# All generated graphs will be saved in this folder.
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def find_data_file(*possible_names):
    """
    Find a dataset in the data folder.
    More than one possible name can be supplied to handle uploaded
    filenames such as 'weather_readings.csv'.
    """
    for filename in possible_names:
        candidate = DATA_DIR / filename
        if candidate.exists():
            return candidate
    print(
        f"[SKIPPED] Could not find any of these files in {DATA_DIR}: "
        + ", ".join(possible_names)
    )
    return None


def save_and_show(filename):
    """Save the current Matplotlib figure, display it, then close it."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()


# ---------------------------------------------------------------------
# PART 1 — LOAD AND INSPECT WEATHER DATA WITH PANDAS
# ---------------------------------------------------------------------

def load_weather_data():
    """Read the weather CSV directly into a Pandas DataFrame."""
    path = find_data_file(
        "weather_readings.csv"
        
    )
    if path is None:
        return None

    weather_df = pd.read_csv(path)

    print("\n" + "=" * 65)
    print("PART 1 — WEATHER DATA: LOAD AND INSPECT")
    print("=" * 65)

    # Display the complete DataFrame.
    print("\nComplete DataFrame:")
    print(weather_df)

    # Display the first five rows.
    print("\nFirst five rows:")
    print(weather_df.head())

    # Display column names.
    print("\nColumn names:")
    print(weather_df.columns)

    # Display data types and non-missing values.
    print("\nDataFrame information:")
    weather_df.info()

    # Display count, mean, standard deviation, minimum, and maximum.
    print("\nNumerical summary:")
    print(weather_df.describe())

    # Check that the expected columns exist before later activities.
    required_columns = ["hour", "measured_temp_c", "model_temp_c"]
    missing_columns = [
        column for column in required_columns
        if column not in weather_df.columns
    ]
    if missing_columns:
        raise ValueError(
            "Weather CSV is missing required columns: "
            + ", ".join(missing_columns)
        )

    # Select columns as Pandas Series.
    hours = weather_df["hour"]
    measured = weather_df["measured_temp_c"]
    model = weather_df["model_temp_c"]

    print("\nSelected hour values:")
    print(hours)
    print("\nSelected measured temperatures:")
    print(measured)

    return weather_df


# ---------------------------------------------------------------------
# PART 2 — ACTIVITY 1: LINE PLOT OF MEASURED TEMPERATURE
# ---------------------------------------------------------------------

def activity1_line_plot(weather_df):
    """Plot measured temperature over the hours of the day."""
    print("\n" + "=" * 65)
    print("PART 2 — ACTIVITY 1: MEASURED TEMPERATURE LINE PLOT")
    print("=" * 65)

    plt.figure(figsize=(8, 5))

    # x-axis: hour; y-axis: measured temperature.
    plt.plot(
        weather_df["hour"],
        weather_df["measured_temp_c"],
        marker="o",
        label="Measured temperature"
    )

    # Add a title, axis labels, grid, and legend.
    plt.title("Measured Temperature During the Day")
    plt.xlabel("Hour of day")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    save_and_show("01_measured_temperature_line.png")

    # Find the hour with the highest measured temperature.
    highest_index = weather_df["measured_temp_c"].idxmax()
    highest_row = weather_df.loc[highest_index]

    print(
        "Highest measured temperature:",
        highest_row["measured_temp_c"],
        "°C at hour",
        highest_row["hour"]
    )


# ---------------------------------------------------------------------
# PART 3 — ACTIVITY 2: COMPARE MEASURED TEMPERATURE WITH MODEL
# ---------------------------------------------------------------------

def activity2_compare_model(weather_df):
    """Plot measured and model temperatures on the same graph."""
    print("\n" + "=" * 65)
    print("PART 3 — ACTIVITY 2: MEASURED VS MODEL TEMPERATURE")
    print("=" * 65)

    plt.figure(figsize=(8, 5))

    # First line: actual measured temperature.
    plt.plot(
        weather_df["hour"],
        weather_df["measured_temp_c"],
        marker="o",
        label="Measured"
    )

    # Second line: model prediction.
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
    plt.grid(True, alpha=0.3)

    save_and_show("02_measured_vs_model.png")

    # Convert the two Pandas Series to NumPy arrays.
    measured_values = weather_df["measured_temp_c"].to_numpy()
    model_values = weather_df["model_temp_c"].to_numpy()

    # Subtract model predictions from measured values, row by row.
    errors = measured_values - model_values

    print("\nPrediction errors (measured - model):")
    print(errors)

    # Absolute error ignores whether the model over- or under-predicted.
    absolute_errors = np.abs(errors)

    # Mean absolute error is the average size of the prediction error.
    mae = np.mean(absolute_errors)

    print(f"Mean absolute error (MAE): {mae:.2f} °C")

    # Identify the row with the largest absolute error.
    largest_error_position = np.argmax(absolute_errors)
    largest_error_row = weather_df.iloc[largest_error_position]

    print(
        "Largest absolute error:",
        f"{absolute_errors[largest_error_position]:.2f} °C",
        "at hour",
        largest_error_row["hour"]
    )


# ---------------------------------------------------------------------
# PART 4 — ACTIVITY 3: REQUIRED SEABORN SCATTER PLOT
# ---------------------------------------------------------------------

def activity3_study_scatter():
    """Use Seaborn to explore the relationship between study hours and scores."""
    print("\n" + "=" * 65)
    print("PART 4 — ACTIVITY 3: SEABORN STUDY HOURS SCATTER PLOT")
    print("=" * 65)

    path = find_data_file("study_hours_scores.csv")
    if path is None:
        return

    study_df = pd.read_csv(path)

    # Inspect the dataset before plotting.
    print("\nFirst five rows:")
    print(study_df.head())

    print("\nDataFrame information:")
    study_df.info()

    print("\nNumerical summary:")
    print(study_df.describe())

    required = ["study_hours", "quiz_score"]
    if not all(column in study_df.columns for column in required):
        print(
            "[SKIPPED] study_hours_scores.csv must contain "
            "'study_hours' and 'quiz_score' columns."
        )
        return

    # Seaborn uses the DataFrame and the column names directly.
    plt.figure(figsize=(7, 5))
    sns.scatterplot(
        data=study_df,
        x="study_hours",
        y="quiz_score"
    )

    plt.title("Study Time and Quiz Score")
    plt.xlabel("Study time (hours)")
    plt.ylabel("Quiz score (%)")
    plt.grid(True, alpha=0.3)

    save_and_show("03_study_hours_vs_quiz_score.png")

    # Calculate the correlation as an additional numerical description.
    # Correlation describes association; it does not prove causation.
    correlation = study_df["study_hours"].corr(study_df["quiz_score"])
    print(f"Correlation between study hours and quiz score: {correlation:.3f}")


# ---------------------------------------------------------------------
# PART 5 — ACTIVITY 4: BAR CHART FOR WEEKLY SALES
# ---------------------------------------------------------------------

def activity4_weekly_sales():
    """Create a bar chart and calculate highest, lowest, and total sales."""
    print("\n" + "=" * 65)
    print("PART 5 — ACTIVITY 4: WEEKLY SALES BAR CHART")
    print("=" * 65)

    path = find_data_file("weekly_sales.csv")
    if path is None:
        return

    sales_df = pd.read_csv(path)

    print("\nFirst five rows:")
    print(sales_df.head())

    print("\nDataFrame information:")
    sales_df.info()

    required = ["day", "units_sold"]
    if not all(column in sales_df.columns for column in required):
        print(
            "[SKIPPED] weekly_sales.csv must contain "
            "'day' and 'units_sold' columns."
        )
        return

    # Create a bar chart with day names on the x-axis.
    plt.figure(figsize=(8, 5))
    plt.bar(
        sales_df["day"],
        sales_df["units_sold"],
        color="skyblue",
        edgecolor="black"
    )

    plt.title("Units Sold by Day")
    plt.xlabel("Day")
    plt.ylabel("Units sold")
    plt.grid(axis="y", alpha=0.3)

    save_and_show("04_weekly_sales_bar.png")

    # Find the maximum and minimum units sold.
    highest = sales_df["units_sold"].max()
    lowest = sales_df["units_sold"].min()

    # Calculate total sales using NumPy.
    total = np.sum(sales_df["units_sold"])

    # idxmax() and idxmin() return the row index labels.
    best_index = sales_df["units_sold"].idxmax()
    worst_index = sales_df["units_sold"].idxmin()

    # Use .loc[] to retrieve the corresponding day.
    best_day = sales_df.loc[best_index, "day"]
    worst_day = sales_df.loc[worst_index, "day"]

    print(f"Highest sales: {highest} units on {best_day}")
    print(f"Lowest sales: {lowest} units on {worst_day}")
    print(f"Total units sold: {total}")


# ---------------------------------------------------------------------
# PART 6 — ACTIVITY 5: HISTOGRAM OF EXAM SCORES
# ---------------------------------------------------------------------

def activity5_exam_histogram():
    """Plot the distribution of exam scores using Matplotlib."""
    print("\n" + "=" * 65)
    print("PART 6 — ACTIVITY 5: EXAM SCORE HISTOGRAM")
    print("=" * 65)

    path = find_data_file("exam_scores.csv")
    if path is None:
        return

    exam_df = pd.read_csv(path)

    print("\nFirst five rows:")
    print(exam_df.head())

    print("\nDataFrame information:")
    exam_df.info()

    print("\nSummary:")
    print(exam_df.describe())

    # The lab specifies that the first column contains exam scores.
    scores = pd.to_numeric(exam_df.iloc[:, 0], errors="coerce").dropna()

    print("Number of scores:", len(scores))
    print("Minimum score:", np.min(scores))
    print("Maximum score:", np.max(scores))
    print("Average score:", np.mean(scores))

    # Matplotlib histogram: six bins, with visible bar boundaries.
    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=6, edgecolor="black", color="skyblue")

    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam score (%)")
    plt.ylabel("Number of students")

    save_and_show("05_exam_scores_histogram.png")


# ---------------------------------------------------------------------
# PART 7 — OPTIONAL KDE DENSITY PLOT FOR EXAM SCORES
# ---------------------------------------------------------------------

def activity6_exam_kde():
    """Create a Seaborn KDE plot using the exam score column."""
    print("\n" + "=" * 65)
    print("PART 7 — OPTIONAL KDE DENSITY PLOT")
    print("=" * 65)

    path = find_data_file("exam_scores.csv")
    if path is None:
        return

    exam_df = pd.read_csv(path)

    # The lab specifies that the first column contains exam scores.
    score_column = exam_df.columns[0]
    exam_df[score_column] = pd.to_numeric(
        exam_df[score_column],
        errors="coerce"
    )
    exam_df = exam_df.dropna(subset=[score_column])

    plt.figure(figsize=(8, 5))

    # KDE is an estimated smooth distribution, not a count histogram.
    sns.kdeplot(
        data=exam_df,
        x=score_column,
        fill=True,
        color="steelblue"
    )

    plt.title("Estimated Distribution of Exam Scores")
    plt.xlabel("Exam score (%)")
    plt.ylabel("Estimated density")

    save_and_show("06_exam_scores_kde.png")


# ---------------------------------------------------------------------
# PART 8 — ACTIVITY 6: CLEAN SENSOR DATA AND PLOT
# ---------------------------------------------------------------------

def activity7_clean_sensor_data():
    """Remove missing and out-of-range sensor values, then plot the data."""
    print("\n" + "=" * 65)
    print("PART 8 — ACTIVITY 6: CLEAN SENSOR DATA")
    print("=" * 65)

    path = find_data_file("sensor_readings_needs_cleaning.csv")
    if path is None:
        return

    sensor_df = pd.read_csv(path)

    print("\nFirst five rows:")
    print(sensor_df.head())

    print("\nDataFrame information:")
    sensor_df.info()

    print("\nMissing values per column:")
    print(sensor_df.isnull().sum())

    # The lab identifies the first column as reading number
    # and the second column as temperature.
    reading_column = sensor_df.columns[0]
    temperature_column = sensor_df.columns[1]

    # Convert the temperature column to numeric values.
    # Invalid text becomes NaN and will be removed by the range filter.
    sensor_df[temperature_column] = pd.to_numeric(
        sensor_df[temperature_column],
        errors="coerce"
    )

    print("\nRows with missing temperature:")
    print(sensor_df[sensor_df[temperature_column].isna()])

    print("\nRows containing the suspicious value 999.0:")
    print(sensor_df[sensor_df[temperature_column] == 999.0])

    # Keep temperatures between 0 and 50 degrees Celsius.
    # NaN values are also excluded because they do not pass the condition.
    clean_df = sensor_df.loc[
        (sensor_df[temperature_column] >= 0)
        & (sensor_df[temperature_column] <= 50)
    ].copy()

    print("\nOriginal number of rows:", len(sensor_df))
    print("Number of valid rows:", len(clean_df))
    print("Number of removed rows:", len(sensor_df) - len(clean_df))

    # Plot the cleaned observations.
    plt.figure(figsize=(8, 5))
    plt.plot(
        clean_df[reading_column],
        clean_df[temperature_column],
        marker="o"
    )

    plt.title("Cleaned Room Temperature Readings")
    plt.xlabel("Reading number")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, alpha=0.3)

    save_and_show("07_cleaned_sensor_readings.png")


# ---------------------------------------------------------------------
# PART 9 — SEABORN ADVANTAGE DEMONSTRATION: CAR CRASH HISTOGRAMS
# ---------------------------------------------------------------------

def activity8_histogram_comparison_car_crashes():
    """
    Compare:
      A. Matplotlib histogram
      B. Seaborn histogram with KDE
      C. Seaborn histogram split by a speeding group

    Seaborn's built-in car_crashes dataset is used for this demonstration.
    """
    print("\n" + "=" * 65)
    print("PART 9 — MATPLOTLIB VS SEABORN HISTOGRAM")
    print("=" * 65)

    try:
        # This is a Seaborn sample dataset.
        # Internet may be needed the first time to download it.
        car_crashes = sns.load_dataset("car_crashes")
    except Exception as error:
        print("[SKIPPED] Could not load Seaborn car_crashes dataset.")
        print("Reason:", error)
        return

    print("\nFirst five rows of car_crashes:")
    print(car_crashes.head())

    # -------------------------------------------------------------
    # 9A — Matplotlib histogram
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 5))

    plt.hist(
        car_crashes["total"],
        bins=8,
        edgecolor="black",
        color="skyblue"
    )

    plt.title("Distribution of Total Car Crashes — Matplotlib")
    plt.xlabel("Total crashes per billion miles")
    plt.ylabel("Number of states")

    # Set the x-axis major tick interval to 2.
    plt.gca().xaxis.set_major_locator(MultipleLocator(2))

    # Set the y-axis major tick interval to 2 states.
    plt.gca().yaxis.set_major_locator(MultipleLocator(2))

    plt.grid(axis="y", alpha=0.3)
    save_and_show("08_car_crashes_matplotlib_histogram.png")

    # -------------------------------------------------------------
    # 9B — Seaborn histogram with KDE
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 5))

    sns.histplot(
        data=car_crashes,
        x="total",
        bins=8,
        kde=True,              # Add a smooth density curve.
        color="steelblue",
        edgecolor="black"
    )

    plt.title("Distribution of Total Car Crashes — Seaborn")
    plt.xlabel("Total crashes per billion miles")
    plt.ylabel("Number of states")

    # Use the same x-axis major interval as the Matplotlib graph.
    plt.gca().xaxis.set_major_locator(MultipleLocator(2))
    plt.grid(axis="y", alpha=0.3)

    save_and_show("09_car_crashes_seaborn_histogram_kde.png")

    # -------------------------------------------------------------
    # 9C — Seaborn histogram comparing two speeding groups
    # -------------------------------------------------------------

    # Calculate the median speeding value.
    median_speeding = car_crashes["speeding"].median()

    # Create a category column:
    # values above the median are "Above median";
    # the rest are "At or below median".
    car_crashes["speeding_group"] = np.where(
        car_crashes["speeding"] > median_speeding,
        "Above median",
        "At or below median"
    )

    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=car_crashes,
        x="total",
        hue="speeding_group",  # Draw a separate distribution for each group.
        bins=8,
        kde=True,
        element="step",
        stat="density",
        common_norm=False,
        alpha=0.3
    )

    plt.title("Crash Distribution by Speeding Group")
    plt.xlabel("Total crashes per billion miles")
    plt.ylabel("Density")

    save_and_show("10_car_crashes_by_speeding_group.png")

    print(
        "\nInterpretation reminder: this graph compares groups. "
        "It does not prove that speeding caused the differences."
    )


# ---------------------------------------------------------------------
# PART 10 — FINAL CHALLENGE TEMPLATE
# ---------------------------------------------------------------------

def final_challenge_template():
    """
    A reusable example of the workflow students should follow:
    load -> inspect -> check missing values -> summarize -> plot -> save.
    This template uses the available weather DataFrame.
    """
    print("\n" + "=" * 65)
    print("PART 10 — FINAL CHALLENGE WORKFLOW (WEATHER EXAMPLE)")
    print("=" * 65)

    path = find_data_file(
        "weather_readings.csv"
         )
    if path is None:
        return

    df = pd.read_csv(path)

    # Inspect the dataset.
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())

    # Calculate a numerical summary using NumPy.
    average_temperature = np.mean(df["measured_temp_c"])
    minimum_temperature = np.min(df["measured_temp_c"])
    maximum_temperature = np.max(df["measured_temp_c"])

    print(f"Average measured temperature: {average_temperature:.2f} °C")
    print(f"Minimum measured temperature: {minimum_temperature:.2f} °C")
    print(f"Maximum measured temperature: {maximum_temperature:.2f} °C")

    # Create a plot suitable for measurements recorded over time.
    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=df,
        x="hour",
        y="measured_temp_c",
        marker="o"
    )

    plt.title("Weather Investigation: Temperature by Hour")
    plt.xlabel("Hour of day")
    plt.ylabel("Measured temperature (°C)")
    plt.grid(True, alpha=0.3)

    save_and_show("11_final_challenge_weather_plot.png")


# ---------------------------------------------------------------------
# MAIN PROGRAM — RUN ALL AVAILABLE ACTIVITIES
# ---------------------------------------------------------------------

def main():
    print("\nLAB 9 — COMPLETE INSTRUCTOR SOLUTION")
    print("Generated figures will be saved in:", OUTPUT_DIR)

    # The weather dataset is supplied with this lab.
    weather_df = load_weather_data()

    # Run weather activities only if the weather CSV was found.
    if weather_df is not None:
        activity1_line_plot(weather_df)
        activity2_compare_model(weather_df)

    # These activities run when their corresponding CSV files are present.
    activity3_study_scatter()
    activity4_weekly_sales()
    activity5_exam_histogram()
    activity6_exam_kde()
    activity7_clean_sensor_data()

    # Seaborn histogram comparison uses Seaborn's sample dataset.
    activity8_histogram_comparison_car_crashes()

    # Demonstrate the final workflow using the supplied weather dataset.
    final_challenge_template()

    print("\n" + "=" * 65)
    print("LAB 9 SOLUTION FINISHED")
    print("Check the outputs folder for generated graph images.")
    print("=" * 65)


if __name__ == "__main__":
    main()
