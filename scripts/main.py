# main.py
import pandas as pd
from recommender import recommend

# Load datasets
billboards = pd.read_csv("data/billboards_dataset.csv")
advertisers = pd.read_csv("data/advertisers_dataset.csv")

# Choose one advertiser
adv = advertisers.iloc[0]  # ADV001

# Get recommendations
top_billboards = recommend(billboards, adv)

print(top_billboards)