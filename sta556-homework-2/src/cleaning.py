"""Reusable cleaning and summary functions for the diabetes analysis."""
import pandas as pd

DIABETES_CUTOFF = 6.5  # glyhb (hemoglobin A1c, %) at or above this means diabetes


def clean_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Rename columns to snake_case and drop the mostly empty second
    blood pressure readings (about 65% missing)."""
    out = data.copy()
    out.columns = [c.replace(".", "_").lower() for c in out.columns]
    out = out.drop(columns=["bp_2s", "bp_2d"])
    return out


def filter_records(data: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate rows and rows missing the key measurements (glyhb, age, weight),
    then add a diabetes flag based on glyhb."""
    out = data.drop_duplicates().dropna(subset=["glyhb", "age", "weight"]).copy()
    out["diabetes"] = (out["glyhb"] >= DIABETES_CUTOFF).map({True: "yes", False: "no"})
    return out.reset_index(drop=True)


def summarize_group(data: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Return count, mean, median and standard deviation of value_col for each group."""
    return (data.groupby(group_col)[value_col]
                .agg(["count", "mean", "median", "std"])
                .round(2))