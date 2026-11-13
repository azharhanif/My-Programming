# Final Group Project 1: Air Quality Monitor & Trend Analyzer

**Course:** Introduction to Python Programming (Science)  
**Project value:** 40 marks  
**Suggested workload:** approximately 10–12 hours

## Scientific context

Analyze PM2.5, PM10, and NO2 readings from monitoring stations. Compare station patterns, identify high-PM2.5 records, and communicate environmental patterns without making unsupported health diagnoses.

## Project goal

Your team will develop one integrated Python program that reads the supplied data, validates it, calculates project-specific measurements, creates visualizations, exports results, and communicates findings.

## Data-science workflow

This project follows the four stages described in OpenStax §15.1:

1. **Data acquisition:** obtain and read the supplied scientific data.
2. **Data exploration:** inspect the data, check its format, and clean or validate records.
3. **Data analysis:** calculate the scientific measurements and summaries required by this project.
4. **Reporting:** communicate results through CSV outputs, graphs, and a written interpretation.

The three project phases organize this workflow: Phase 1 focuses on acquisition and exploration; Phase 2 focuses on analysis; Phase 3 focuses on visualization and reporting. These stages are iterative: if a graph or calculation reveals a data problem, return to the relevant earlier step and correct it.

## Required Pandas implementation and academic-integrity rule

Your program must use Pandas DataFrames for CSV data acquisition, exploratory data analysis (EDA), data cleaning, filtering, feature creation, grouping/summary analysis, and CSV export. A solution that uses only `csv.reader()`, Python lists, and `csv.writer()` does not meet the project requirements.

At minimum, demonstrate the Pandas techniques taught in Lab 8 and the related class material:

- `import pandas as pd` and `pd.read_csv()` to load tabular data.
- `head()`, `info()`, `describe()`, column selection, and `loc[]` / `iloc[]` to inspect data.
- `isnull().sum()`, `dropna()`, and/or `fillna()` to identify and handle missing data. Explain why your chosen strategy is appropriate; do not replace meaningful missing outcomes with invented values.
- Boolean filtering with `&` and `|`, `sort_values()`, and derived columns/features.
- `groupby()` with aggregation where a project summary by station, patient, region, sample, or other category is required.
- `to_csv(index=False)` to export cleaned data and analysis results.

Use Matplotlib for the required figures and animations. You may use ordinary Python functions, loops, and lists where they are appropriate for scientific algorithms (for example, peak detection, motif scanning, or numerical simulation), but Pandas must remain the primary tool for tabular data work. Do not use SciPy, scikit-learn, Plotly, BioPython, or external scientific/signal-processing libraries unless the instructor approves them. 


## Team organization

Your group decides how to divide the work. You must maintain a brief contribution log describing who worked on which parts, how the code was integrated, and how each member verified the final program. All members remain responsible for understanding the complete project.

## Serial phase requirement

The project is completed in three dependent phases. **Phase 1 must be submitted and accepted before Phase 2 begins. Phase 2 must be submitted and accepted before Phase 3 begins.** Phase 2 must extend the Phase 1 program, and Phase 3 must extend the Phase 2 program. Do not replace the earlier work with unrelated separate scripts.



### Required Pandas evidence in every phase

- **Phase 1:** Load the supplied tabular data with `pd.read_csv()`. Show `head()`, `info()`, `describe()`, and `isnull().sum()`. Use `loc[]` or `iloc[]` to inspect records. Identify malformed or missing values and create a cleaned DataFrame using an explained `dropna()` / `fillna()` / filtering strategy. (For the FASTA project, use Python file reading for sequence text, then create a DataFrame for sequence metadata and validation results.)
- **Phase 2:** Use DataFrame boolean filtering, `sort_values()`, derived columns, and `groupby()` aggregation for at least one project-specific calculation or summary. Do not calculate every summary solely by manually iterating over lists.
- **Phase 3:** Use DataFrame columns and grouped/filtered DataFrames as the source for plots and exports. Save cleaned and derived tables with `to_csv(index=False)`. Your report must identify at least three Pandas operations and explain what each contributed to the analysis.

### Phase 1 — Data acquisition, inspection, and validation (12 marks)

Complete the following tasks: Read and inspect the CSV; validate pollutant values and dates..

**Required outputs:** a working `project.py`, a cleaned/validated CSV export, a short `phase1_notes.md`, and at least one basic labelled plot.


### Phase 2 — Scientific calculations and summary outputs (14 marks)

After Phase 1 is accepted, extend the same program to complete the following: Calculate mean PM2.5, PM10, and NO2 by station using loops and lists. Flag PM2.5 readings greater than 25 μg/m³..

**Required outputs:** the Phase 1 outputs plus the project-specific metric and summary CSV files, calculation notes, and at least one additional plot.


### Phase 3 — Visualization, animation, and interpretation (14 marks)

After Phase 2 is accepted, extend the same program to complete the following: Create a PM2.5 time-series plot, pollutant distribution histogram, PM10-versus-NO2 scatter plot, and a 3D plot using time/index, PM2.5, and PM10. Animate PM2.5 progression. Export anomaly and station-summary CSV files..

**Required outputs:** the complete project folder, all required PNG plots, one MP4 animation using the Lecture 11 `FuncAnimation` workflow, exported CSV files, a 2–4 page report or presentation, and a README with run instructions.


## Final deliverables

- `project.py` — integrated program for all three phases.
- `data/` — supplied input data; do not overwrite the original files.
- `outputs/` — generated CSV files, PNG plots, and MP4 animation.
- A contribution log. The group chooses its own division of work.

## Suggested assessment breakdown — 40 marks

| Phase | Assessment focus | Marks |
|---|---|---:|
| Phase 1 | Correct file loading, inspection, validation, initial output and explanation | 12 |
| Phase 2 | Correct scientific calculations, summary tables, validation and extension of Phase 1 | 14 |
| Phase 3 | Graphs, animation, exports, interpretation, and integration | 14 |
| **Total** | | **40** |

The post-submission challenges are separate individual verification activities. The instructor may assess them separately from the 40-mark project grade.


## Project-specific required outputs

- Read and inspect the CSV; validate pollutant values and dates.
- Calculate mean PM2.5, PM10, and NO2 by station using loops and lists. Flag PM2.5 readings greater than 25 μg/m³.
- Create a PM2.5 time-series plot, pollutant distribution histogram, PM10-versus-NO2 scatter plot, and a 3D plot using time/index, PM2.5, and PM10. Animate PM2.5 progression. Export anomaly and station-summary CSV files.

## Output filenames

The reference solution uses the following filenames. Your output names may differ if they are clearly documented and all required content is present.

**CSV exports:**
- `cleaned_air_quality.csv`
- `anomalies.csv`
- `summary_by_station.csv`

**PNG figures:**
- `pm25_timeseries.png`
- `pm25_distribution.png`
- `pm10_no2_scatter.png`
- `air_quality_3d.png`

**MP4 animation:**
- `pm25_animation.mp4`

## Scientific interpretation requirements

- State what each calculated measure means and show the formula or algorithm used.
- Distinguish observations from interpretations.
- Identify at least two limitations of the supplied data or simplified model.
- Do not make clinical, public-health, regulatory, or biological claims beyond what the synthetic/teaching data support.
- Label every plot with a meaningful title and axis labels, including units where appropriate.

## Folder structure

```text
P01_Air_Quality/
├── STUDENT_HANDOUT.md
├── project.py
├── README.md
├── data/
└── outputs/
```

## Installation and execution

```bash
python -m pip install pandas matplotlib
python project.py
```

For Phase 3 MP4 animation export, Lecture 11 uses FFmpeg. Install FFmpeg and make sure it is available to Python before calling `ani.save(..., writer="ffmpeg")`. If FFmpeg is unavailable, demonstrate the animation with `plt.show()` and arrange export with the instructor.


## Required implementation approach

Use Pandas as the required tabular-data workflow. Begin with `df = pd.read_csv(...)`; inspect with `head()`, `info()`, `describe()`, and `isnull().sum()`; select columns; use `loc[]` / `iloc[]`; filter rows with Boolean conditions; clean missing or invalid data; create derived columns; summarize with `groupby()`; and export with `to_csv(index=False)`. Use Matplotlib for plots. Ordinary Python loops/functions may supplement Pandas for project-specific algorithms that are not naturally expressed as DataFrame operations.
