import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

frames = []
for file in sorted(DATA_DIR.glob("*.csv")):
    df = pd.read_csv(file)
    df["Site"] = file.stem
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    frames.append(df)

raw = pd.concat(frames, ignore_index=True)

def warning_mask(df):
    return ((df["pH"] < 6.5) | (df["pH"] > 8.5) | (df["Dissolved_Oxygen_mgL"] < 7) | (df["Turbidity_NTU"] > 8))

summaries = []
detailed = []
for site, df in raw.groupby("Site"):
    df = df.sort_values("Timestamp").reset_index(drop=True).copy()
    df["Warning"] = warning_mask(df)
    df["Temp_Rolling"] = df["Temperature_C"].rolling(window=3, min_periods=1).mean()
    df["DO_Change"] = df["Dissolved_Oxygen_mgL"].diff()
    df["Sudden_Jump"] = (df["Temperature_C"].diff().abs() > 1.2) | (df["Turbidity_NTU"].diff().abs() > 2.0)
    summaries.append({
        "Site": site,
        "Mean_Temp": round(df["Temperature_C"].mean(), 2),
        "Mean_pH": round(df["pH"].mean(), 2),
        "Mean_DO": round(df["Dissolved_Oxygen_mgL"].mean(), 2),
        "Max_DO": round(df["Dissolved_Oxygen_mgL"].max(), 2),
        "Min_DO": round(df["Dissolved_Oxygen_mgL"].min(), 2),
        "Warning_Count": int(df["Warning"].sum()),
        "First_Warning_Time": str(df.loc[df["Warning"], "Timestamp"].iloc[0]) if df["Warning"].any() else "None"
    })
    detailed.append(df)

detailed_df = pd.concat(detailed, ignore_index=True)
summary_df = pd.DataFrame(summaries).sort_values("Warning_Count")
detailed_df.to_csv(OUTPUT_DIR / "combined_water_data.csv", index=False)
summary_df.to_csv(OUTPUT_DIR / "phase_summary.csv", index=False)

one = detailed_df[detailed_df["Site"] == detailed_df["Site"].iloc[0]]
plt.figure(); plt.plot(one["Timestamp"], one["Temperature_C"]); plt.xticks(rotation=45); plt.savefig(OUTPUT_DIR / "temp_plot.png", bbox_inches="tight"); plt.close()
plt.figure(); plt.plot(one["Timestamp"], one["pH"]); plt.xticks(rotation=45); plt.savefig(OUTPUT_DIR / "ph_plot.png", bbox_inches="tight"); plt.close()
plt.figure(); plt.plot(one["Timestamp"], one["Dissolved_Oxygen_mgL"]); plt.xticks(rotation=45); plt.savefig(OUTPUT_DIR / "oxygen_plot.png", bbox_inches="tight"); plt.close()

plt.figure(figsize=(10,8))
plt.subplot(2,2,1); plt.plot(one["Timestamp"], one["Temperature_C"]); plt.xticks(rotation=45); plt.title("Temp")
plt.subplot(2,2,2); plt.plot(one["Timestamp"], one["Turbidity_NTU"]); plt.xticks(rotation=45); plt.title("Turbidity")
plt.subplot(2,2,3); plt.bar(summary_df["Site"], summary_df["Warning_Count"]); plt.title("Warnings")
plt.subplot(2,2,4); plt.bar(summary_df["Site"], summary_df["Mean_DO"]); plt.title("Mean DO")
plt.tight_layout(); plt.savefig(OUTPUT_DIR / "water_dashboard.png", bbox_inches="tight"); plt.close()

(OUTPUT_DIR / "phase3_report.txt").write_text(
    f"Best site by fewest warnings: {summary_df.iloc[0]['Site']}\nWorst site by warnings: {summary_df.iloc[-1]['Site']}\n",
    encoding="utf-8"
)
print(summary_df)
