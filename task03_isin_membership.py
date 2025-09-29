"""
Task 3 — .isin() Membership
Goal: Keep rows with city in {"Tashkent","Jizzakh","Bukhara"}
"""
import pandas as pd

def make_df():
    return pd.DataFrame({
        "name": ["Madina", "Sardor", "Akmal", "Shoxrux", "Nodira"],
        "city": ["Bukhara","Namangan","Tashkent","Jizzakh","Tashkent"]
    })

def task3(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: use .isin on 'city'
    # Example: df[df["city"].isin({"Tashkent","Jizzakh","Bukhara"})]
    raise NotImplementedError

if __name__ == "__main__":
    df = make_df()
    out = task3(df)
    assert set(out["city"]).issubset({"Tashkent","Jizzakh","Bukhara"})
    print("PASS: task3")
