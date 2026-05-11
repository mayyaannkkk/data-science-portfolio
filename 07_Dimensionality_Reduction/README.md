# Dimensionality Reduction -- PCA, t-SNE, UMAP

**Course:** DSA 506 Visual Analytics and Communications
**Datasets:** Breast Cancer (Wisconsin), Digits (MNIST subset), Wine Quality

## Overview
Comparative study applying three dimensionality reduction methods to three high-dimensional datasets with class labels.

## Methods
| Method | Type | Key Hyperparameter |
|--------|------|--------------------|
| PCA | Linear | n_components, explained variance |
| t-SNE | Non-linear | perplexity |
| UMAP | Non-linear | n_neighbors, min_dist |

## For Each Dataset
- 2D scatter plot color-coded by class
- PCA cumulative explained variance curve
- Written interpretation after every visualization

## Files
| File | Description |
|------|-------------|
| `dimensionality_reduction.ipynb` | Full notebook |

## Tech Stack
Python, Scikit-learn, UMAP-learn, Matplotlib, Seaborn, Jupyter/Colab
