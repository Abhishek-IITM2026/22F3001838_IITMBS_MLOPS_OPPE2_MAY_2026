import pandas as pd
from scipy.stats import ks_2samp

train = pd.read_csv("data.csv")
sample = pd.read_csv("sample_100.csv")

numeric_cols = [
    col for col in train.columns
    if pd.api.types.is_numeric_dtype(train[col])
]

print("Checking drift...\n")

for col in numeric_cols:

    train_col = train[col].dropna().values
    sample_col = sample[col].dropna().values

    stat, p = ks_2samp(train_col, sample_col)

    if p < 0.05:
        print(f"{col}: DRIFT DETECTED (p={p:.4f})")
    else:
        print(f"{col}: No significant drift (p={p:.4f})")
