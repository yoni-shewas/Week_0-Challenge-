from data_cleaning import clean_data
import pandas as pd


benin = "data/benin-malanville.csv"
sierraLeone = "data/sierraleone-bumbuna.csv"
togo = "data/togo-dapaong_qc.csv"

clean_data(benin)
clean_data(sierraLeone)
clean_data(togo)


benin_cleaned = pd.read_csv(f"cleaned_data/{benin}")
sierraLeone_cleaned = pd.read_csv(f"cleaned_data/{sierraLeone}")
togo_cleaned = pd.read_csv(f"cleaned_data/{togo}")
