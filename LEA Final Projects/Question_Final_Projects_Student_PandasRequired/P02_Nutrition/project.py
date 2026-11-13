"""Student starter. Pandas is required for tabular data work.
Complete each phase only after the previous phase has been checked.
"""
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA_FOLDER = Path("data")
OUTPUT_FOLDER = Path("outputs")
OUTPUT_FOLDER.mkdir(exist_ok=True)

def phase1_load_inspect_validate():
    # TODO: Load with pd.read_csv(DATA_FOLDER / "YOUR_DATA_FILE.csv").
    # TODO: Inspect with head(), info(), describe(), isnull().sum().
    # TODO: Use loc[] / iloc[] and create a cleaned DataFrame.
    # Example: df = pd.read_csv(DATA_FOLDER / "YOUR_DATA_FILE.csv")
    pass

def phase2_calculate_export():
    # TODO: Use Boolean filtering, sort_values(), derived columns, and groupby().
    # TODO: Export DataFrames with to_csv(..., index=False).
    pass

def phase3_visualize_animate_report():
    # TODO: Build plots from filtered/grouped DataFrame columns.
    # TODO: Export final tables with DataFrame.to_csv(index=False).
    # TODO: Add 3D plots/FuncAnimation only where specified by the handout.
    pass

if __name__ == "__main__":
    phase1_load_inspect_validate()
    # Uncomment Phase 2 only after Phase 1 is complete and accepted.
    # phase2_calculate_export()
    # Uncomment Phase 3 only after Phase 2 is complete and accepted.
    # phase3_visualize_animate_report()
