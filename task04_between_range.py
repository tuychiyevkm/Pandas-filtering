"""
Task 4 — between Range
Goal: salary between 10_000 and 25_000 inclusive
"""
import pandas as pd

def make_df():
    return pd.DataFrame({
        "name":   ["A", "B", "C", "D", "E"],
        "salary": [9000, 12000, 18000, 26000, 24000]
    })

def task4(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: use .between on 'salary'
    # Example: df[df["salary"].between(10_000, 25_000, inclusive="both")]
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task4(df)
    assert out["salary"].between(10_000, 25_000, inclusive="both").all()
    print("PASS: task4")
