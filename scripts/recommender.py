# recommender.py
import pandas as pd

def score_billboard(billboard, advertiser):
    audience_score = 1 if billboard["preferred_audience"] == advertiser["target_audience"] else 0.5
    budget_score = 1 if billboard["monthly_cost"] <= advertiser["budget"] else 0
    footfall_score = billboard["estimated_footfall"] / 20000

    final_score = (audience_score * 0.4) + (budget_score * 0.3) + (footfall_score * 0.3)
    return round(final_score, 3)

def recommend(df_billboards, advertiser):
    df = df_billboards.copy()
    df["score"] = df.apply(lambda row: score_billboard(row, advertiser), axis=1)
    return df.sort_values(by="score", ascending=False).head(10)

import pandas as pd

# Load datasets
billboards = pd.read_csv("data/billboards_dataset.csv")
advertisers = pd.read_csv("data/advertisers_dataset.csv")

# Scoring function
def score_billboard(billboard, advertiser):
    audience_score = 1 if billboard["preferred_audience"] == advertiser["target_audience"] else 0.5
    budget_score = 1 if billboard["monthly_cost"] <= advertiser["budget"] else 0
    footfall_score = billboard["estimated_footfall"] / 20000

    return round((audience_score * 0.4) + (budget_score * 0.3) + (footfall_score * 0.3), 3)

# Create results dictionary
results = {}

# For each advertiser, score and get top 10 billboards
for _, adv in advertisers.iterrows():
    billboards["score"] = billboards.apply(lambda row: score_billboard(row, adv), axis=1)
    top_10 = billboards.sort_values(by="score", ascending=False).head(10)
    results[adv["advertiser_id"]] = top_10

    # Save each to CSV
    top_10.to_csv(f"data/top_recommendations_{adv['advertiser_id']}.csv", index=False)

print("✅ Recommendations generated for all advertisers.")