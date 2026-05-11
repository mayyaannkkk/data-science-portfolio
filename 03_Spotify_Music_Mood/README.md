# Spotify Music & Mood -- Multi-Modal Storytelling

**Course:** DSA 506 Visual Analytics and Communications
**Type:** Final Project | **Dataset:** 114,000+ Spotify tracks

## Research Question
Do people who listen to "sad" music experience worse emotional outcomes, or does the data tell a different story? This project investigates the "Sad Banger" phenomenon -- tracks that are low in valence but high in energy.

## Data Types Used
| Type | Content |
|------|---------|
| Numerical | Valence, energy, tempo, danceability, loudness |
| Categorical | Genre, key, mode, explicit flag |
| Text | Track names and artist names via NLP and sentiment analysis |
| Image | Album art dominant color extraction via PIL |

## Storytelling Structure
1. Hook -- surprising streaming stat during mental health dips
2. Context -- what Spotify audio features actually measure
3. Conflict -- challenging the assumption that sad music = harmful
4. Analysis -- PCA/t-SNE/UMAP mood landscape, clustering, sentiment
5. Resolution -- the Sad Banger cluster and emotional regulation findings
6. Call to action -- implications for playlist design and music therapy

## Tech Stack
Python, Pandas, Scikit-learn, UMAP-learn, NetworkX, Matplotlib, Seaborn, PIL, Jupyter/Colab
