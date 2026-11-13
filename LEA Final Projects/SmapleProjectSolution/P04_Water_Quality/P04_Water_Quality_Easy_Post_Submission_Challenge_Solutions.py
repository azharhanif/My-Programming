"""
P04 Water Quality — Instructor Solutions for Three Short Challenges

Place this file beside the original project.py:
    P04_Water_Quality/
        project.py
        challenge_solutions.py
        data/water_samples.csv

This script reuses the original project's load_clean() and analyze()
functions rather than reimplementing the project.
"""

import matplotlib.pyplot as plt
from pathlib import Path

# Reuse the functions from the actual P04 project solution.
import project


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def phase1_highest_nitrate(clean_df):
    """Challenge 1: show the valid sample with the highest nitrate value."""
    highest_row = clean_df.loc[clean_df["Nitrate_mg_L"].idxmax()]

    print("\nPHASE 1 — Highest nitrate sample")
    print(highest_row[["SiteID", "Date", "Nitrate_mg_L"]])


def phase2_highest_site_average(site_summary):
    """Challenge 2: show the site with the highest mean nitrate."""
    highest_site = site_summary.loc[site_summary["Mean_Nitrate"].idxmax()]

    print("\nPHASE 2 — Site with the highest average nitrate")
    print(highest_site[["SiteID", "Mean_Nitrate"]])


def phase3_plot_average_nitrate(site_summary):
    """Challenge 3: plot the existing per-site mean nitrate values."""
    plt.figure(figsize=(8, 5))
    plt.bar(site_summary["SiteID"], site_summary["Mean_Nitrate"])
    plt.title("Average Nitrate Concentration by Site")
    plt.xlabel("Site ID")
    plt.ylabel("Mean nitrate (mg/L)")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    output_file = OUTPUT_DIR / "phase3_mean_nitrate_by_site.png"
    plt.savefig(output_file)
    plt.close()

    print("\nPHASE 3 — Bar chart saved to:", output_file)


def main():
    # Phase 1: use the original project's data loading and cleaning function.
    clean_df = project.load_clean()
    phase1_highest_nitrate(clean_df)

    # Phase 2: use the original project's analysis and site summary.
    analyzed_df, site_summary, anomalies = project.analyze(clean_df)
    phase2_highest_site_average(site_summary)

    # Phase 3: visualize the summary already calculated in Phase 2.
    phase3_plot_average_nitrate(site_summary)


if __name__ == "__main__":
    main()
