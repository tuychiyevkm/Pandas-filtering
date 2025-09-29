"""
Task 5 — String Contains
Goal: Names that contain "ov" (case-insensitive)
"""
import pandas as pd

def make_df():
    return pd.DataFrame({
        "name": ["Aliyev", "Komron", "Akbarov", "Madina", "Nodira"]
    })

def task5(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: use .str.contains("ov", case=False, na=False)
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task5(df)
    assert out["name"].str.contains("ov", case=False, na=False).all()
    print("PASS: task5")
