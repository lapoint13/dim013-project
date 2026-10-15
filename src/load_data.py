import sys

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame.

    Args:
        path: Relative path to the CSV file.

    Returns:
        The loaded data.
    """
    return pd.read_csv(path, sep=",", encoding="utf-8-sig")


def summarize_data(df: pd.DataFrame) -> None:
    """Print a summary of a DataFrame.

    Args:
        df: The DataFrame to summarize.
    """
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")


if __name__ == "__main__":
    print(load_data(sys.argv[1]).head())
