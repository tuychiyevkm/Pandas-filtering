"""
Task 6 — Missing Values
Goal: Drop rows where score is NaN (only this column matters)
"""
import pandas as pd
import numpy as np

def make_df():
    return pd.DataFrame({
        "name":  ["Ali", "B", "C", "D", "E"],
        "score": [np.nan, 65, 72, np.nan, 81]
    })

def task6(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: drop rows with NaN in 'score' only
    # Example: df.dropna(subset=["score"])
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task6(df)
    assert not out["score"].isna().any()
    print("PASS: task6")
