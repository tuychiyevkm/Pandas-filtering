"""
Task 7 — query API
Goal: age >= 18 and city == 'Tashkent' using df.query(...)
"""
import pandas as pd

def make_df():
    return pd.DataFrame({
        "name": ["Aliyev", "Komron", "Dilshod", "Zarina", "Akbarov"],
        "age":  [17,       19,        21,        16,       25],
        "city": ["Tashkent","Jizzakh", "Tashkent","Samarkand","Tashkent"]
    })

def task7(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: use query string
    # Example: df.query("age >= 18 and city == 'Tashkent'")
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task7(df)
    assert (out["age"] >= 18).all() and (out["city"] == "Tashkent").all()
    print("PASS: task7")
