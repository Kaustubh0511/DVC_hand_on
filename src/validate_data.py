import sys
from pathlib import Path

import pandas as pd

TRAIN_PATH = Path("data/processed/train.csv")

EXPECTED_COLUMNS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "target"
]

def main() -> int :
    if not TRAIN_PATH.exists():
        print(f"Error: {TRAIN_PATH} does not exist. Please run the data preparation step first.")
        return 1

    df = pd.read_csv(TRAIN_PATH)

    #1 Column Check
    cols = list(df.columns)
    if cols != EXPECTED_COLUMNS:
        print(f"Error: Columns in {TRAIN_PATH} do not match expected columns.")
        # print(f"Expected: {EXPECTED_COLUMNS}")
        # print(f"Found: {cols}")
        return 1

    # NUll Check
    null_counts = df.isnull().sum()
    if null_counts.any():
        print(f"Error: Found null values in {TRAIN_PATH}.")
        print(null_counts[null_counts > 0])
        return 1

    print(f"Data validation passed for {TRAIN_PATH}.")
    return 0

if __name__ == "__main__":
    sys.exit(main())