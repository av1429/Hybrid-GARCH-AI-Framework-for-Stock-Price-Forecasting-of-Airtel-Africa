project:
  title: "📈 Hybrid GARCH–AI Framework for Stock Price Forecasting of Airtel Africa"

  overview: >
    This project presents a hybrid econometric–AI framework for predicting Airtel Africa’s stock prices
    by integrating Generalized Autoregressive Conditional Heteroskedasticity (GARCH) models with modern
    deep learning architectures such as LSTM, GRU, Transformer, BiGRU, and GRU-Attention.
    The goal is to combine statistical volatility modeling with neural sequence learning
    for more accurate and interpretable financial forecasting.

  key_features:
    - Combines GARCH-based volatility modeling with AI models for robust forecasting.
    - Implements 10 models including LSTM, GRU, Transformer, and novel hybrids (BiGRU–GARCH, GRU–Attention).
    - Evaluated using RMSE, MAE, MAPE, and R² metrics on Airtel Africa stock data (2019–2024).
    - Achieved R² = 0.8898 and RMSE = 3.26 using the GRU–Attention (30-day lookback) model.
    - Fully implemented in Google Colab using Python, TensorFlow, Scikit-learn, and Statsmodels.

  model_architectures:
    base_models: ["LSTM", "GRU", "Transformer"]
    hybrid_models: ["GARCH–LSTM", "GARCH–GRU", "GARCH–Transformer"]
    novel_models: ["BiGRU", "BiGRU–GARCH", "GRU–Attention", "GRU–Attention–GARCH"]
    best_model:
      name: "GRU–Attention (30-day lookback)"
      metrics:
        RMSE: 3.26
        MAE: 2.07
        MAPE: "2.13%"
        R2: 0.8898
      notes: "Outperformed all baseline and hybrid GARCH models."

  data_collection:
    source: "Yahoo Finance"
    ticker: "Airtel Africa (AAF.L)"
    period: "June 2019 – May 2024"
    attributes: ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    preprocessing:
      - Handle missing data using forward-fill interpolation.
      - Compute log returns and rolling volatility (5-day window).
      - Normalize features using StandardScaler (Z-score normalization).
      - Split data chronologically (67% train / 33% test).
      - Generate time sequences (30, 60, 90, 120 days) for model inputs.

  dataset_access:
    description: >
      The dataset is directly imported in the Colab notebook using the Yahoo Finance API.
      Users can replicate the same dataset retrieval with the following Python snippet.
    code: |
      from pandas_datareader import data as pdr
      import yfinance as yf
      yf.pdr_override()
      df = pdr.get_data_yahoo('AAF.L', start='2019-06-28', end='2024-05-08')
    note: "No manual dataset upload required."

  results_summary:
    description: "Performance comparison of all implemented models."
    metrics:
      - model: "GRU"
        RMSE: 3.29
        MAE: 2.48
        MAPE: "2.16%"
        R2: 0.863
      - model: "GRU–GARCH"
        RMSE: 3.30
        MAE: 2.48
        MAPE: "2.16%"
        R2: 0.863
      - model: "LSTM"
        RMSE: 5.98
        MAE: 4.67
        MAPE: "4.11%"
        R2: 0.55
      - model: "LSTM–GARCH"
        RMSE: 5.81
        MAE: 4.49
        MAPE: "4.00%"
        R2: 0.58
      - model: "BiGRU"
        RMSE: 5.57
        MAE: 4.50
        MAPE: "4.07%"
        R2: 0.61
      - model: "GRU–Attention"
        RMSE: 3.26
        MAE: 2.07
        MAPE: "2.13%"
        R2: 0.89

  key_takeaway: >
    Integrating attention mechanisms outperformed traditional volatility modeling,
    enabling more dynamic short-term forecasts with improved predictive stability.

  tools_and_libraries:
    languages: ["Python"]
    frameworks: ["TensorFlow", "Keras", "Scikit-learn", "Statsmodels"]
    data_source: "Yahoo Finance"
    platform: "Google Colab (GPU Enabled)"
    visualization: ["Matplotlib", "Seaborn"]

  future_enhancements:
    - Integrate macroeconomic indicators (CPI, GDP, interest rates).
    - Implement ensemble methods and multi-asset training.
    - Extend attention-based hybridization for cryptocurrency and commodity markets.
    - Add explainability using SHAP and LIME for interpretability.

  authors:
    - name: "Aravinthvasan S"
      role: "Data collection, GARCH–AI integration, GRU-Attention architecture, result visualization."
    - name: "Gade V S S L Keertana"
      role: "GRU/Transformer implementation, evaluation."
    - name: "Sasmita K G"
      role: "Literature survey, documentation, and reporting."

  license:
    type: "MIT License"
    description: >
      This repository is open-source under the MIT License.
      Feel free to use, modify, and build upon this work with proper attribution.

  keywords:
    - "GARCH"
    - "Stock Forecasting"
    - "Airtel Africa"
    - "GRU"
    - "Attention Mechanism"
    - "Deep Learning"
    - "Hybrid AI"
    - "Financial Time Series"
