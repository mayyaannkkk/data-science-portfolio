# EEG Seizure Detection -- Neural Networks

**Course:** Machine Learning
**Dataset:** EEG seizure detection dataset (Kaggle)
**Target:** 93%+ accuracy, under 1 minute runtime per model

## Overview
Built and compared three neural network architectures for classifying EEG signals as seizure vs non-seizure events.

## Models
| Model | Architecture | API |
|-------|-------------|-----|
| Model 1 | Feed-forward with BatchNorm and Dropout | Sequential API |
| Model 2 | Multi-branch parallel dense layers | Functional API |
| Model 3 | Multi-task with auxiliary classification head | Functional API + Auxiliary Output |

## Techniques
- EarlyStopping, ReduceLROnPlateau, ModelCheckpoint callbacks
- PCA for dimensionality reduction pre-training
- StandardScaler normalization pipeline
- HeNormal weight initialization
- L1/L2 regularization

## Results
All three models: 93%+ accuracy, under 1 minute runtime in Google Colab.

## Files
| File | Description |
|------|-------------|
| `eeg_seizure_detection.ipynb` | Full notebook with all 3 models |

## How to Run
1. Open in Google Colab (Python runtime)
2. Upload Kaggle API token when prompted
3. Run all cells -- dataset downloads automatically

## Tech Stack
Python, TensorFlow/Keras, Scikit-learn, MNE, Pandas, NumPy, Google Colab
