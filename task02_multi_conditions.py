"""
Task 2 — Multiple Conditions
Goal: age >= 18 AND city == "Tashkent"
"""
import pandas as pd

def make_df():
    return pd.DataFrame({
        "name": ["Aliyev", "Komron", "Dilshod", "Zarina", "Akbar"],
        "age":  [17,       19,        21,        16,       25],
        "city": ["Tashkent","Jizzakh", "Tashkent","Samarkand","Tashkent"]
    })

def task2(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: combine conditions with & and parentheses
    # Example: df[(df["age"] >= 18) & (df["city"] == "Tashkent")]
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task2(df)
    assert (out["age"] >= 18).all() and (out["city"] == "Tashkent").all()
    print("PASS: task2")
