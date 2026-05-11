# Mayank Waghmare — Data Science Portfolio

**MS Data Science Analytics | SUNY Polytechnic Institute, Utica NY**  
**Graduate Assistant — Dept. of Computer and Information Sciences**  
📧 mayankwaghmare23@gmail.com | 📞 (480) 685-1911

---

## About

I am a graduate student specializing in data science, machine learning, and computational research. I currently serve as a Graduate Assistant under Prof. Amir Manzourolajdad, working on RNA structural analysis using graph neural networks and deep learning pipelines. This portfolio collects projects from my graduate coursework, research assistantship, and independent work.

**Core skills:** Python, R, PyTorch, Scikit-learn, NetworkX, Streamlit, SQL, Tableau, Power BI, DSSR, AlphaFold workflows.

---

## Projects

| # | Project | Domain | Tools |
|---|---------|--------|-------|
| 1 | [Stanford RNA 3D Folding — Kaggle Competition](#1-stanford-rna-3d-folding--kaggle-competition) | Computational Biology / ML | Python, PyTorch, CNN, Transformer |
| 2 | [RNA Inverse Design — GNN Research (GA Work)](#2-rna-inverse-design--gnn-research-ga-work) | Computational Biology / Research | Python, DSSR, AlphaFold, GNN |
| 3 | [Spotify Music & Mood — Multi-Modal Storytelling](#3-spotify-music--mood--multi-modal-storytelling) | Visual Analytics | Python, PCA, t-SNE, UMAP, NetworkX |
| 4 | [Argentina Football Analytics Dashboard](#4-argentina-football-analytics-dashboard) | Sports Analytics / Dashboarding | Python, Streamlit, Plotly, GitHub |
| 5 | [Social Network Analysis](#5-social-network-analysis) | Network Science | Python, NetworkX, Plotly |
| 6 | [Premier League 2³ Factorial Experimental Design](#6-premier-league-2k-factorial-experimental-design) | Statistics / Experimental Design | R, ANOVA, RCBD |
| 7 | [Dimensionality Reduction — PCA, t-SNE, UMAP](#7-dimensionality-reduction--pca-t-sne-umap) | Machine Learning | Python, Scikit-learn |
| 8 | [Visual EDA — NYPD Motor Vehicle Collisions](#8-visual-eda--nypd-motor-vehicle-collisions) | Data Visualization | R, ggplot2 |
| 9 | [Logistics Network Mapping](#9-logistics-network-mapping) | Geospatial Analytics | Python, Folium, Matplotlib |
| 10 | [EEG Seizure Detection — Neural Networks](#10-eeg-seizure-detection--neural-networks) | Biomedical ML | Python, TensorFlow/Keras |

---

## 1. Stanford RNA 3D Folding — Kaggle Competition

**Folder:** `01_RNA_3D_Folding/`  
**Course:** Machine Learning | **Team:** Team Shuttle

Competed in the Stanford RNA 3D Folding Kaggle competition, which challenges participants to predict the 3D coordinates of RNA molecules from their nucleotide sequences. Built a hybrid CNN + Transformer architecture with a secondary structure prediction module based on the Nussinov algorithm.

- Preprocessed raw RNA sequence data into numerical feature representations
- Implemented a Nussinov dynamic programming algorithm for secondary structure prediction
- Designed a two-notebook pipeline: preprocessing + final model submission
- Evaluated using TM-score (Template Modeling score)

**Tech stack:** Python, PyTorch, NumPy, Pandas, Matplotlib  
**Kaggle score:** 0.129 (TM-score)

---

## 2. RNA Inverse Design — GNN Research (GA Work)

**Folder:** `02_RNA_GNN_Research/`  
**Role:** Graduate Assistant | **Advisor:** Prof. Amir Manzourolajdad

Active research contribution in the Department of Computer and Information Sciences at SUNY Polytechnic Institute. Work is centered on the lab's publication: *Secondary-Structure-Informed RNA Inverse Design via Relational Graph Neural Networks* (Manzourolajdad & Mohebbi, MDPI 2025).

- Run structural analysis pipelines on PDB and mmCIF files using DSSR (v2.4.2) to extract base pairs, helices, stems, loops, G-quadruplexes, pseudoknots, and torsion angles
- Contribute to the relational GNN architecture for sequence-to-structure RNA inverse design
- Coordinate AlphaFold-based structural validation workflows
- Maintain reproducible computational notebooks aligned with research publication goals

**Tech stack:** Python, DSSR v2.4.2, PDB/mmCIF processing, AlphaFold (web server), PyTorch

---

## 3. Spotify Music & Mood — Multi-Modal Storytelling

**Folder:** `03_Spotify_Music_Mood/`  
**Course:** DSA 506 — Visual Analytics and Communications | Final Project

End-to-end visual analytics storytelling project on 114,000+ Spotify tracks. Research question: *Do people who listen to "sad" music experience worse emotional outcomes — or is the opposite true?*

Analyzed four data types: numerical audio features (valence, energy, tempo), categorical metadata (genre, key, mode), text (track names, artist names via NLP), and image data (album art color extraction).

- Hook: surprising statistic about streaming patterns during depression peaks
- Built PCA, t-SNE, and UMAP visualizations to map the "mood landscape" of music
- Used k-means clustering to discover natural genre-mood groupings
- Built NetworkX artist collaboration graphs showing genre bridges
- Sentiment analysis on track names; album art dominant color extraction via PIL
- Investigated the "Sad Banger" phenomenon — high-energy low-valence tracks

**Tech stack:** Python, Pandas, Scikit-learn, Matplotlib, Seaborn, NetworkX, PIL, Jupyter

---

## 4. Argentina Football Analytics Dashboard

**Folder:** `04_Argentina_Football_Dashboard/`  
**Course:** DSA 506 — Visual Analytics and Communications

Interactive multi-page dashboard built with Streamlit and deployed on Streamlit Community Cloud via GitHub. Analyzes Argentina's international football match data from 1872 to 2025.

- Sidebar filters for year range and tournament type
- KPI cards: total matches, win rate, goals scored/conceded
- Decade-level performance trends (line charts)
- Opponent breakdown (top rivals, head-to-head records)
- Penalty shootout analysis
- Humanized interpretations alongside each visualization

**Tech stack:** Python, Streamlit, Plotly, Pandas, GitHub  
**Live app:** *(Streamlit Community Cloud deployment)*  
**Dataset:** Kaggle — International Football Results 1872–2025

---

## 5. Social Network Analysis

**Folder:** `05_Social_Network_Analysis/`  
**Course:** DSA 506 — Visual Analytics and Communications

Analyzed a 100-user social network dataset to answer questions about influence, connectivity, and community structure.

- Identified top influencers using degree centrality and betweenness centrality
- Computed shortest paths between key node pairs
- Detected communities using the Louvain algorithm
- Built treemap visualizations for sector-level membership breakdown
- Humanized interpretations after every chart

**Tech stack:** Python, NetworkX, Plotly, Matplotlib, community (python-louvain)

---

## 6. Premier League 2k Factorial Experimental Design

**Folder:** `06_Premier_League_Factorial_Design/`  
**Course:** DSA 503 — Data Collection and Design of Experiments

Designed and analyzed a real-data 2³ factorial experiment using Premier League match data. Research question: *How do pressing intensity (PPDA), home advantage, and possession percentage interact to affect goals scored?*

- Factors: Pressing intensity (high/low), Home/Away, Possession (high/low) — 2 levels each
- Season treated as a blocking variable (RCBD structure)
- Built full 2³ factorial ANOVA table by hand and verified with `aov()` in R
- Applied residual diagnostics (normality, homogeneity of variance)
- Applied Prof. Thistleton's 6-step hypothesis testing framework throughout
- Compared full interaction model vs. reduced main-effects-only model

**Tech stack:** R (Google Colab R-kernel), ggplot2, agricolae  
**Dataset:** Real EPL match data from Kaggle / FBref

---

## 7. Dimensionality Reduction — PCA, t-SNE, UMAP

**Folder:** `07_Dimensionality_Reduction/`  
**Course:** DSA 506 — Visual Analytics and Communications

Comparative study of three dimensionality reduction techniques applied to three high-dimensional datasets: Breast Cancer (Wisconsin), Digits (MNIST subset), and Wine Quality.

- Applied PCA, t-SNE, and UMAP on each dataset
- Visualized 2D embeddings with cluster color-coding
- Explained variance plots for PCA components
- Compared cluster separation and computation time across methods
- Humanized written interpretation after each visualization

**Tech stack:** Python, Scikit-learn, UMAP-learn, Matplotlib, Seaborn, Jupyter/Colab

---

## 8. Visual EDA — NYPD Motor Vehicle Collisions

**Folder:** `08_Visual_EDA_NYPD/`  
**Course:** DSA 506 — Visual Analytics and Communications

Exploratory data analysis with storytelling on the NYPD Motor Vehicle Collisions dataset using R and ggplot2 in a Google Colab R-kernel notebook.

- Time-of-day collision heatmaps
- Borough-level bar and density plots
- Injury vs. fatality breakdowns
- Contributing factor frequency analysis
- Full narrative structure: hook, context, conflict, resolution

**Tech stack:** R, ggplot2, dplyr, tidyr, Colab R-kernel

---

## 9. Logistics Network Mapping

**Folder:** `09_Logistics_Mapping/`  
**Course:** DSA 506 — Visual Analytics and Communications

Geospatial analytics project mapping a logistics network of warehouses, customers, and delivery routes across the US.

- Haversine-based distance calculations between nodes
- Folium interactive maps with warehouse coverage radius circles
- Route optimization visualization (under/over 200-mile threshold)
- Capacity utilization bubble maps
- Demand analysis with priority-quadrant scatter plots

**Tech stack:** Python, Folium, Pandas, NumPy, Matplotlib, Jupyter/Colab

---

## 10. EEG Seizure Detection — Neural Networks

**Folder:** `10_EEG_Seizure_Detection/`  
**Course:** Machine Learning

Built and compared three neural network architectures for EEG-based seizure detection, targeting 93%+ accuracy with each model running under 1 minute.

- Model 1: Sequential API — standard feed-forward with BatchNorm and Dropout
- Model 2: Functional API — multi-branch architecture with parallel dense layers
- Model 3: Functional API with Auxiliary Output — multi-task learning with auxiliary classification head
- All models use EarlyStopping, ReduceLROnPlateau, and ModelCheckpoint callbacks
- Data loading via Kaggle API in Google Colab

**Tech stack:** Python, TensorFlow/Keras, Scikit-learn, MNE, Pandas, Colab

---

## Education

**MS Data Science Analytics** — SUNY Polytechnic Institute, Utica NY *(Expected 2026)*  
Coursework: Big Data Analytics, Statistics for Data Analytics, Machine Learning, Graphical Neural Computation, Visual Analytics and Communications, Data Collection and Design of Experiments, Data Mining, Multidimensional Signal Processing

**B.Tech Electrical Engineering** — Yeshwantrao Chavan College of Engineering, Nagpur *(2024)*

---

## Professional Experience

- **Graduate Assistant** — SUNY Poly, Dept. of Computer and Information Sciences *(Aug 2025 – Present)*
- **Assistant Project Manager Intern** — Makalu, Dubai *(Mar 2024 – Jul 2024)*
- **Data Analyst Intern** — Life of Riley Pvt. Ltd., Delhi *(Jul 2023 – Sep 2023)*

---

*Last updated: May 2026*
