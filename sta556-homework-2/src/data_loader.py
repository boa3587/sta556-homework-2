"""Load the raw diabetes data reproducibly using a path relative to the project root."""
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "diabetes.csv"

EXPECTED_COLUMNS = ["id", "chol", "stab.glu", "hdl", "ratio", "glyhb", "location",
                    "age", "gender", "height", "weight", "frame", "bp.1s", "bp.1d",
                    "bp.2s", "bp.2d", "waist", "hip", "time.ppn"]


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Read the raw CSV and check that it has the expected columns.

    Raises FileNotFoundError with download instructions if the file is missing.
    """
    if not Path(path).exists():
        raise FileNotFoundError(
            f"{path} not found. Download diabetes.csv from "
            "https://www.kaggle.com/datasets/imtkaggleteam/diabetes and put it in data/."
        )
    data = pd.read_csv(path)
    missing = set(EXPECTED_COLUMNS) - set(data.columns)
    if missing:
        raise ValueError(f"Unexpected file layout; missing columns: {sorted(missing)}")
    return data


def inspect_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return a table of dtype, missing count and missing percent for each column."""
    return pd.DataFrame({
        "dtype": data.dtypes.astype(str),
        "n_missing": data.isna().sum(),
        "pct_missing": (data.isna().mean() * 100).round(1),
    })