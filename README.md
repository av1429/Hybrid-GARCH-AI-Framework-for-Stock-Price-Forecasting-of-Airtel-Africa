# 📈 Hybrid GARCH–AI Framework for Stock Price Forecasting of Airtel Africa

## 📄 Overview
This project develops a **hybrid econometric–AI framework** for forecasting the stock prices of **Airtel Africa (AAF.L)** by combining traditional **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)** volatility modeling with advanced **deep learning architectures** such as **LSTM, GRU, Transformer, BiGRU, and GRU–Attention**.

The goal is to fuse **statistical volatility analysis** with **temporal neural sequence modeling** to achieve more accurate, interpretable, and stable financial predictions.  
All experiments were implemented and tested in **Google Colab** using data directly fetched from **Yahoo Finance**.

---

## ⚙️ Features & Highlights
- 📊 **Hybrid Modeling:** Combines econometric (GARCH) and deep learning approaches for robust forecasting.  
- 🤖 **Multi-Model Comparison:** Implements 10 models including LSTM, GRU, Transformer, BiGRU–GARCH, GRU–Attention, and GRU–Attention–GARCH.  
- 📈 **Evaluation Metrics:** RMSE, MAE, MAPE, and R² across all model architectures.  
- 🧠 **Best Model:** GRU–Attention (30-day lookback) achieved **R² = 0.8898** and **RMSE = 3.26**.  
- ☁️ **Platform:** Python (TensorFlow, Scikit-learn, Statsmodels) on Google Colab.  
- 💹 **Data Source:** Airtel Africa stock data (2019–2024) from **Yahoo Finance**.

---

## 🧩 Model Architectures

| Type | Models | Description |
|------|---------|-------------|
| **Base Models** | LSTM, GRU, Transformer | Deep sequence models for time-series forecasting. |
| **Hybrid Models** | GARCH–LSTM, GARCH–GRU, GARCH–Transformer | Combine statistical volatility with deep learning. |
| **Novel Models** | BiGRU, BiGRU–GARCH, GRU–Attention, GRU–Attention–GARCH | Enhanced hybrid networks using bidirectional and attention layers. |

> 🏆 **Best Performing Model:** GRU–Attention (30-day lookback) — achieved highest accuracy, stability, and lowest error metrics across all tests.

---

## 🧮 Data Collection & Preprocessing
- **Source:** Yahoo Finance  
- **Ticker:** `AAF.L` (Airtel Africa PLC)  
- **Period:** June 2019 – May 2024  
- **Attributes:** Date, Open, High, Low, Close, Adj Close, Volume  

### 🔧 Preprocessing Steps
1. Handle missing data via forward-fill interpolation.  
2. Compute **log returns** and **rolling volatility (5-day window)**.  
3. Normalize features using **StandardScaler** (Z-score normalization).  
4. Split dataset chronologically: 67% training / 33% testing.  
5. Generate sequence windows with lookback periods of **30, 60, 90, and 120 days**.

---

## 📦 Dataset Access
The dataset is **automatically imported** from Yahoo Finance 
✅ No manual uploads required — data is directly pulled from the source at runtime.

---

## ✅ Key Insight:
The GRU–Attention model achieved the most accurate results, outperforming both pure deep learning and GARCH-hybrid models.
Its attention mechanism effectively captured temporal volatility patterns and short-term dependencies.

--- 

## 🧠 Tools & Environment

- **Language:** Python
- **Frameworks:**  TensorFlow, Keras, Scikit-learn, Statsmodels
- **Data Source:** Yahoo Finance API
- **Platform:** Google Colab (GPU Enabled)
- **Visualization:** Matplotlib, Seaborn

---

## 🚀 Future Enhancements

- Integrate macroeconomic indicators (CPI, GDP, interest rates).
- Introduce ensemble approaches for improved generalization.
- Extend hybrid attention modeling to cryptocurrencies and commodities.
- Apply explainable AI (XAI) tools such as SHAP and LIME for transparency.

---

## 👨‍💻 Authors

- **Aravinthvasan S**
B.Tech ECE (Cyber-Physical Systems), SASTRA Deemed University  
Role: Data collection, GARCH–AI integration, GRU–Attention architecture, and visualization.
 🔗 **GitHub:** [GitHub Profile](https://github.com/av1429)

- **Gade V S S L Keertana** — GRU/Transformer implementation and performance evaluation.
- **Sasmita K G** — Literature survey, documentation, and result analysis.

---

## 🪪 License
This project is licensed under the MIT License — you are free to use, modify, and distribute this work with proper attribution.

---

## 🏷️ Keywords

`GARCH` · `Stock Forecasting` · `Airtel Africa` · `GRU` · `Attention Mechanism` · `Deep Learning` · `Hybrid AI` · `Financial Time Series`
