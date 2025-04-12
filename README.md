# Carbon-Aware Energy Forecasting with XGBoost

This repository contains the code and datasets used in our publication on short-term energy forecasting using environmental features such as weather and carbon intensity. The models include both traditional ML (XGBoost) and deep learning (LSTM) approaches to evaluate predictive performance and model transferability.

## 📁 Project Structure

```
.
├── data/             # Raw data files (weather.csv, carbon_intensity.csv, etc.)
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

## 📈 Outputs

All generated plots will be saved in the `figures/` folder.

## 📜 License

MIT License.
