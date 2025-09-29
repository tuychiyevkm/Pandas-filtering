"""
Task 1 — Basic Boolean Filter
Goal: Keep rows where age >= 18
"""
import pandas as pd
import numpy as np

def make_df():
    return pd.DataFrame({
        "name": ["Ali", "Komron", "Dilshod", "Zarina"],
        "age":  [17,     19,       21,        16],
        "city": ["Tashkent","Jizzakh","Tashkent","Samarkand"]
    })

def task1(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: return only rows where age >= 18
    # Example: df[ df["age"] >= 18 ]
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task1(df)
    assert (out["age"] >= 18).all()
    print("PASS: task1")
