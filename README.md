# 🎯 Smart Billboard Recommender

A small recommender system that helps advertisers choose the **best billboard placements** for a campaign. Each billboard is scored on how well it matches an advertiser's target audience, budget and expected foot traffic. The results are explored in an interactive **Streamlit** dashboard.

Built by **Arletes Shajilal** (aivancity School for Technology, Business & Society, Paris) during an internship at **Egerine**.

---

## ✨ Features

- **Scoring engine** that ranks every billboard for a given advertiser
- **Top-10 recommendations** per advertiser, exported to CSV
- **Streamlit dashboard** with three tabs:
  - 📈 Recommendations: a sortable table plus a CSV download
  - 📊 Analytics: billboards per city, foot-traffic distribution, and type × environment breakdown
  - 📄 About the project
- **Synthetic dataset generator** covering billboards, advertisers and historical campaigns

## 🧮 How the scoring works

```
score = 0.4 × audience_match + 0.3 × within_budget + 0.3 × (footfall / 20 000)
```

| Component | Value |
|---|---|
| `audience_match` | 1.0 if the billboard's preferred audience equals the advertiser's target, else 0.5 |
| `within_budget` | 1 if the monthly cost ≤ the advertiser's budget, else 0 |
| `footfall` | Estimated monthly foot traffic, normalised to 0–1 |

## 📁 Project structure

```
smart-billboard-recommender/
├── app.py                      # Streamlit dashboard
├── requirements.txt
├── data/
│   ├── billboards_dataset.csv      # billboard id, city, location, type, environment, footfall, cost, audience
│   ├── advertisers_dataset.csv     # advertiser id, target audience, budget
│   ├── historical_campaigns.csv    # past campaigns: views, clicks, season, budget
│   └── top_recommendations_ADV00X.csv   # generated top-10 per advertiser
└── scripts/
    ├── generate_data.py        # scores all advertisers and writes the top-10 CSVs
    ├── recommender.py          # reusable score_billboard() / recommend() functions
    └── main.py                 # example: recommendations for one advertiser
```

## ▶️ Run it locally

```bash
git clone https://github.com/rlx06/smart-billboard-recommender.git
cd smart-billboard-recommender
pip install -r requirements.txt

# (optional) regenerate the recommendation CSVs
python scripts/generate_data.py

# launch the dashboard
streamlit run app.py
```

The repo also includes a `.devcontainer`, so you can open it in **GitHub Codespaces** and the app starts automatically on port 8501.

## 🛠️ Tech stack

Python · pandas · NumPy · scikit-learn · Streamlit · Matplotlib · Seaborn

## 🔭 Possible next steps

- Let users pick the advertiser in the sidebar instead of the fixed `ADV001` example
- Show billboards on a map (latitude/longitude are already in the data)
- Learn the score weights from `historical_campaigns.csv` (views/clicks) instead of fixing them by hand
