"""
Task 8 — Date Filtering
Goal: Keep rows in March 2025 (inclusive)
"""
import pandas as pd

def make_df():
    dates = pd.date_range("2025-02-20", periods=40, freq="D")
    return pd.DataFrame({"date": dates, "value": range(1, len(dates)+1)})

def task8(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: filter dates between 2025-03-01 and 2025-03-31 inclusive
    # Example:
    # start, end = pd.Timestamp("2025-03-01"), pd.Timestamp("2025-03-31")
    # df[(df["date"] >= start) & (df["date"] <= end)]
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task8(df)
    assert out["date"].between("2025-03-01","2025-03-31", inclusive="both").all()
    print("PASS: task8")
