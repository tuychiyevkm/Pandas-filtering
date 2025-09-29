"""
Task 10 — Group Filter
Goal: Keep groups (by city) whose mean(score) > 70
"""
import pandas as pd
import numpy as np

def make_df():
    return pd.DataFrame({
        "name":  ["A","B","C","D","E","F","G","H"],
        "city":  ["Tashkent","Tashkent","Jizzakh","Jizzakh","Bukhara","Bukhara","Tashkent","Jizzakh"],
        "score": [80, 75, 65, 72, 90, 55, 78, 74]
    })

def task10(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: use groupby("city").filter with lambda g: g["score"].mean() > 70
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task10(df)
    # Verify each remaining group's mean > 70
    for c, g in out.groupby("city"):
        assert g["score"].mean() > 70
    print("PASS: task10")
