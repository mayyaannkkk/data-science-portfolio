# Argentina Football Analytics Dashboard

**Course:** DSA 506 Visual Analytics and Communications
**Deployment:** Streamlit Community Cloud via GitHub
**Dataset:** International Football Results 1872-2025 (Kaggle)

## Overview
Interactive multi-page Streamlit dashboard analyzing Argentina's complete international football history across 150+ years of match data.

## Features
- Year range and tournament filters in the sidebar
- KPI cards: total matches, wins, draws, losses, win rate, goals
- Decade-level performance trend lines
- Head-to-head records against top rivals
- Penalty shootout analysis
- Humanized interpretations alongside every chart

## Running Locally
```bash
git clone https://github.com/YOUR_USERNAME/argentina-football-dashboard
cd argentina-football-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Files
| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `results.csv` | Match results 1872-2025 |
| `goalscorers.csv` | Goal scorer data |
| `shootouts.csv` | Penalty shootout outcomes |

## Tech Stack
Python, Streamlit, Plotly, Pandas, NumPy, GitHub
