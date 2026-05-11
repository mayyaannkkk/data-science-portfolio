# Stanford RNA 3D Folding -- Kaggle Competition

**Course:** Machine Learning | **Team:** Team Shuttle
**Competition:** [Stanford RNA 3D Folding](https://www.kaggle.com/competitions/stanford-rna-3d-folding)

## Overview
Predicted 3D coordinates of RNA molecules from nucleotide sequences using a hybrid CNN + Transformer architecture. Secondary structure was predicted using a custom Nussinov dynamic programming algorithm before 3D coordinate regression.

## Architecture
- Preprocessing notebook: sequence encoding, Nussinov secondary structure prediction, feature engineering
- Model notebook: CNN feature extractor -> Transformer encoder -> 3D coordinate regression head
- Evaluation metric: TM-score (Template Modeling score)
- Kaggle score: 0.129

## Files
| File | Description |
|------|-------------|
| `notebook1_preprocessing.ipynb` | Sequence loading, Nussinov algorithm, feature engineering |
| `notebook2_final_model.ipynb` | CNN + Transformer model, training, submission generation |

## How to Run
1. Open either notebook in Kaggle or Google Colab
2. Connect to the Stanford RNA 3D Folding competition dataset
3. Run all cells top to bottom
4. Notebook 2 generates `submission.csv`

## Tech Stack
Python, PyTorch, NumPy, Pandas, Matplotlib, Kaggle Notebooks
