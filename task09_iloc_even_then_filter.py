"""
Task 9 — iloc Even Rows, then Filter
Goal: Take even-index rows using iloc (0,2,4,...) then keep rows where score > 70
"""
import pandas as pd
import numpy as np

def make_df():
    return pd.DataFrame({
        "name": ["A","B","C","D","E","F"],
        "score":[55,72,68,91,70,83]
    })

def task9(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: even_rows = df.iloc[::2]; then filter score > 70
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task9(df)
    even_idx = df.index[::2]
    assert set(out.index).issubset(set(even_idx))
    assert (out["score"] > 70).all()
    print("PASS: task9")
