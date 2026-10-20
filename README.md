# STA 556 Homework 2: Diabetes Data Pipeline

## Purpose
A small, reproducible Python pipeline that reads an external dataset, cleans it with reusable
functions, and shows one clear finding visually.

## Data Source
Kaggle "Diabetes" dataset (`diabetes.csv`) by Mohamadreza Momeni,
https://www.kaggle.com/datasets/imtkaggleteam/diabetes, accessed October 17, 2026.
Raw data on rural African-American patients (403 rows, 19 columns).
License: "Other (specified in description)" on Kaggle.
Original study: [fill in from the Kaggle data dictionary]

**How to obtain the data:** download `diabetes.csv` from the Kaggle page above (free account
required) and place it in `data/`.

## How to Run
1. `pip install -r requirements.txt`
2. Put `diabetes.csv` in `data/`
3. Open `notebooks/analysis.ipynb` and run all cells

## Project Structure
- `data/`: raw data
- `src/`: reusable functions (`data_loader.py`, `cleaning.py`)
- `notebooks/`: the analysis notebook
- `figures/`: saved plots

## Main Finding
Stabilized glucose is the strongest correlate of glycosylated hemoglobin (r = 0.74). Patients
with diabetes (glyhb of 6.5 or higher; 64 of 389 patients) had a median glucose of about 183
mg/dL versus 86 mg/dL for those without, and were older (median age about 59.5 versus 41).
Diabetes prevalence was similar across gender and county.