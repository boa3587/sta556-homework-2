# STA 556 Homework 2: Diabetes Data Pipeline

## Purpose
A small, reproducible Python pipeline that reads an external dataset, cleans it with reusable
functions, and shows one clear finding visually.

## Data Source
Kaggle "Diabetes" dataset (`diabetes.csv`) by Mohamadreza Momeni,
https://www.kaggle.com/datasets/imtkaggleteam/diabetes, accessed October 17, 2026.
Raw data on rural African-American patients in central Virginia (403 rows, 19 columns).
License: "Other (specified in description)" on Kaggle.

Original study: Willems JP, Saunders JT, Hunt DE, Schorling JB. Prevalence of coronary heart
disease risk factors among rural blacks: a community-based study. Southern Medical Journal.
1997;90:814-820.

**Data:** `diabetes.csv` is included in `data/`. The original file can also be downloaded
from the Kaggle page above (free account required).

## How to Run
1. `pip install -r requirements.txt`
2. Confirm `diabetes.csv` is in `data/`
3. Open `notebooks/analysis.ipynb` from the `notebooks/` folder and run all cells

## Project Structure
- `data/`: raw data
- `src/`: reusable functions (`data_loader.py`, `cleaning.py`)
- `notebooks/`: the analysis notebook
- `figures/`: saved plots

## Cleaning Notes
Diabetes is defined as glycosylated hemoglobin (`glyhb`) of 6.5% or higher, the standard
clinical threshold. Rows missing `glyhb`, `age` or `weight` were removed (14 of 403), and the
two mostly empty second blood pressure columns were dropped.

## Main Finding
Stabilized glucose is the strongest correlate of glycosylated hemoglobin (r = 0.74). Patients
with diabetes (64 of 389 patients) had a median glucose of about 183 mg/dL versus 86 mg/dL for
those without, and were older (median age about 59.5 versus 41). Diabetes prevalence was
similar across gender and county.

![Glycosylated hemoglobin vs stabilized glucose](figures/fig3_glyhb_vs_glucose.png)