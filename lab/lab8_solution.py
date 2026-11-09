import pandas as pd


def part_a_and_b(df):
    print("\n--- PART A: INSPECTION ---")
    print(df.head())
    df.info()
    print(df.describe())
    print(df[["student_id", "study_hours", "quiz_score"]])
    print(df["quiz_score"])

    print("\n--- PART B: INDEXING ---")
    print(df.iloc[0])
    print(df.iloc[2])
    print(df.iloc[0, 1])
    print(df.iloc[:5])
    print(df.iloc[:3, :2])

    print(df.loc[4])
    print(df.loc[4, "study_hours"])
    print(df.loc[0:4])
    print(df.loc[0:4, ["student_id", "quiz_score"]])


def part_c(df):
    print("\n--- PART C: FILTERING ---")
    high_study = df[df["study_hours"] >= 4]
    print(high_study)
    print("At least 4 study hours:", len(high_study))

    selected = df[
        (df["study_hours"] >= 3) &
        (df["quiz_score"] >= 75)
    ]
    print(selected)

    either_condition = df[
        (df["study_hours"] >= 5) |
        (df["quiz_score"] >= 90)
    ]
    print(either_condition)

    print(df.sort_values("quiz_score", ascending=False).head())


def part_d(df):
    print("\n--- PART D: MISSING DATA ---")
    print(df.isnull())
    print(df.isnull().sum())

    missing_rows = df[df.isnull().any(axis=1)]
    print(missing_rows)

    complete_df = df.dropna()
    print("Rows before:", len(df))
    print("Rows after dropna:", len(complete_df))

    filled_df = df.copy()
    filled_df["study_hours"] = filled_df["study_hours"].fillna(
        filled_df["study_hours"].mean()
    )
    filled_df["attendance_percent"] = filled_df["attendance_percent"].fillna(
        filled_df["attendance_percent"].mean()
    )
    print(filled_df.loc[[9, 10, 11]])


def part_e(df):
    print("\n--- PART E: FEATURE CREATION ---")
    feature_df = df.copy()
    feature_df["study_category"] = pd.NA

    feature_df.loc[
        feature_df["study_hours"] < 2, "study_category"
    ] = "Low"

    feature_df.loc[
        (feature_df["study_hours"] >= 2) &
        (feature_df["study_hours"] < 4), "study_category"
    ] = "Moderate"

    feature_df.loc[
        feature_df["study_hours"] >= 4, "study_category"
    ] = "High"

    print(feature_df[["student_id", "study_hours", "study_category"]])
    print(feature_df["study_category"].value_counts())

    plot_df = df.dropna(subset=["study_hours", "quiz_score"])
    print(plot_df[["study_hours", "quiz_score"]])


def part_f():
    print("\n--- PART F: LAB ENVIRONMENT ---")
    environment_df = pd.read_csv("data/lab_environment.csv")
    print(environment_df.head())
    environment_df.info()
    print(environment_df.isnull().sum())

    print(environment_df[environment_df["lab_temperature_c"].isnull()])

    ok_rows = environment_df[environment_df["sensor_status"] == "OK"]
    print(ok_rows)

    valid_environment = environment_df[
        (environment_df["sensor_status"] == "OK") &
        (environment_df["lab_temperature_c"].notnull())
    ]
    print(valid_environment)


def main():
    df = pd.read_csv("data/class_progress.csv")
    part_a_and_b(df)
    part_c(df)
    part_d(df)
    part_e(df)
    part_f()


if __name__ == "__main__":
    main()
