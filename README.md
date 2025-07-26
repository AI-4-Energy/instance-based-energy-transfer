# Carbon-Aware Energy Forecasting with XGBoost

This repository contains the code and datasets used in our publication on short-term energy forecasting using environmental features such as weather and carbon intensity. The models include both traditional ML (XGBoost) and deep learning (LSTM) approaches to evaluate predictive performance and model transferability.

## 📁 Project Structure

```
.
├── data/             # Raw data files, result CSVs and pre-trained models
├── figures/          # Output plots and visualizations
├── src/              # Core scripts for loading, processing, and modeling
├── Code_Base.ipynb   # Jupyter notebook
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/AI-4-Energy/instance-based-energy-transfer.git
cd instance-based-energy-transfer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the notebook:
```bash
jupyter notebook Code_Baseipynb
```

## 🧠 Model Overview

- **Model**: XGBoost Regressor
- **Inputs**: Temperature, humidity, carbon intensity, etc.
- **Output**: Predicted energy consumption
- **Tools**: pandas, seaborn, matplotlib, xgboost


## Model Configurations

### XGBoost
- Boosting rounds: 100
- Learning rate: 0.1
- Max depth: 6
- Early stopping: 10 rounds on validation set

### LSTM
- Layers: 2
- Units per layer: 50
- Dropout: 0.2
- Optimizer: Adam (lr = 0.001)
- Batch size: 32
- Epochs: up to 50
- Early stopping: 5 rounds

Hyperparameters were selected based on a grid search and validation.


## 📈 Outputs

All generated plots will be saved in the `figures/` folder.

## 📜 License

MIT License.
