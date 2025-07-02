# generate_data.py
import pandas as pd
import numpy as np
import random

# Set seed
random.seed(42)
np.random.seed(42)

cities = ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice']
environments = ['Urban', 'Suburban', 'Highway', 'Commercial', 'Residential']
billboard_types = ['Static', 'Digital', 'Mobile']
audience_profiles = ['Youth', 'Families', 'Professionals', 'Tourists', 'General']

# Billboard Dataset
billboards = []
for i in range(200):
    billboards.append({
        "billboard_id": f"BB{i+1:03d}",
        "city": random.choice(cities),
        "lat": round(np.random.uniform(43.0, 49.0), 6),
        "lon": round(np.random.uniform(1.5, 7.5), 6),
        "type": random.choice(billboard_types),
        "environment": random.choice(environments),
        "estimated_footfall": random.randint(500, 20000),
        "monthly_cost": random.randint(500, 5000),
        "preferred_audience": random.choice(audience_profiles)
    })
df_billboards = pd.DataFrame(billboards)
df_billboards.to_csv("data/billboards_dataset.csv", index=False)

# Advertisers Dataset
advertisers = [
    {"advertiser_id": "ADV001", "target_audience": "Youth", "budget": 8000},
    {"advertiser_id": "ADV002", "target_audience": "Professionals", "budget": 15000},
    {"advertiser_id": "ADV003", "target_audience": "Families", "budget": 5000},
    {"advertiser_id": "ADV004", "target_audience": "Tourists", "budget": 12000},
    {"advertiser_id": "ADV005", "target_audience": "General", "budget": 10000},
]
df_advertisers = pd.DataFrame(advertisers)
df_advertisers.to_csv("data/advertisers_dataset.csv", index=False)

# Historical Campaigns
campaigns = []
for i in range(100):
    campaigns.append({
        "campaign_id": f"CPG{i+1:03d}",
        "advertiser_id": random.choice(df_advertisers["advertiser_id"]),
        "billboard_id": f"BB{random.randint(1, 200):03d}",
        "duration_days": random.randint(7, 30),
        "total_views": random.randint(1000, 100000),
        "clicks": random.randint(50, 3000),
        "season": random.choice(["Spring", "Summer", "Autumn", "Winter"]),
        "budget": random.randint(1000, 15000)
    })
df_campaigns = pd.DataFrame(campaigns)
df_campaigns.to_csv("data/historical_campaigns.csv", index=False)

print("✅ All datasets generated!")

import pandas as pd
import numpy as np
import random

# Set seed
random.seed(42)
np.random.seed(42)

# Billboard data
cities = ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice']
environments = ['Urban', 'Suburban', 'Highway', 'Commercial', 'Residential']
billboard_types = ['Static', 'Digital', 'Mobile']
audience_profiles = ['Youth', 'Families', 'Professionals', 'Tourists', 'General']

billboards = []
for i in range(200):
    billboards.append({
        "billboard_id": f"BB{i+1:03d}",
        "city": random.choice(cities),
        "lat": round(np.random.uniform(43.0, 49.0), 6),
        "lon": round(np.random.uniform(1.5, 7.5), 6),
        "type": random.choice(billboard_types),
        "environment": random.choice(environments),
        "estimated_footfall": random.randint(500, 20000),
        "monthly_cost": random.randint(500, 5000),
        "preferred_audience": random.choice(audience_profiles)
    })

df_billboards = pd.DataFrame(billboards)
df_billboards.to_csv("data/billboards_dataset.csv", index=False)

# Advertiser dataset
advertisers = [
    {"advertiser_id": "ADV001", "target_audience": "Youth", "budget": 8000},
    {"advertiser_id": "ADV002", "target_audience": "Professionals", "budget": 15000},
    {"advertiser_id": "ADV003", "target_audience": "Families", "budget": 5000},
    {"advertiser_id": "ADV004", "target_audience": "Tourists", "budget": 12000},
    {"advertiser_id": "ADV005", "target_audience": "General", "budget": 10000},
]
df_advertisers = pd.DataFrame(advertisers)
df_advertisers.to_csv("data/advertisers_dataset.csv", index=False)

# Historical campaigns
campaigns = []
for i in range(100):
    campaigns.append({
        "campaign_id": f"CPG{i+1:03d}",
        "advertiser_id": random.choice(df_advertisers["advertiser_id"]),
        "billboard_id": f"BB{random.randint(1, 200):03d}",
        "duration_days": random.randint(7, 30),
        "total_views": random.randint(1000, 100000),
        "clicks": random.randint(50, 3000),
        "season": random.choice(["Spring", "Summer", "Autumn", "Winter"]),
        "budget": random.randint(1000, 15000)
    })

df_campaigns = pd.DataFrame(campaigns)
df_campaigns.to_csv("data/historical_campaigns.csv", index=False)

print("✅ All datasets generated and saved.")