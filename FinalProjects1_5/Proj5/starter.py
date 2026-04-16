import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_csv(path):
    return pd.read_csv(path)

def main():
    print("Complete the TODOs for this project.")

if __name__ == "__main__":
    main()
