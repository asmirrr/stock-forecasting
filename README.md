# stock-forecasting

**Predicting Next-Day Stock Prices with Linear Regression and Technical Features**

## Overview

This project explores whether simple statistical signals derived from historical price data, such as moving averages, returns, and volatility, can be used to predict the **next trading day’s closing price** of a stock using a linear regression model.

Rather than attempting to “beat the market,” the purpose of this project is to understand:

* How time-series data can be transformed into machine learning features
* Why linear models struggle with financial markets
* How trend inertia influences short-term price movement

The result is a clean, end-to-end pipeline from data acquisition to prediction and evaluation.

---

## What This Project Demonstrates

* Financial data collection with `yfinance`
* Feature engineering from raw time-series price data
* Proper train/test splitting for time-dependent data
* Building and evaluating a regression model with `scikit-learn`
* Visual comparison of predicted vs actual prices
* Practical limitations of linear regression in market prediction

---

## Features Used for Prediction

From daily closing prices, the following features are created:

* 7-day moving average (MA7)
* 30-day moving average (MA30)
* Daily percentage return
* 7-day rolling volatility
* Current closing price

The model attempts to predict **tomorrow’s closing price** using today’s signals.

---

## Installation

```bash
pip install yfinance pandas numpy scikit-learn matplotlib
```

---

## How to Run

Simply execute the script:

```bash
python main.py
```

The program will:

1. Download historical data for the chosen stock
2. Engineer predictive features
3. Train a linear regression model
4. Output the Mean Absolute Error (MAE)
5. Predict the next trading day’s closing price
6. Display a plot comparing predictions to actual values

---

## Results

You will observe that:

* The model loosely tracks price trends
* Predictions lag during sharp market moves
* Error increases during high volatility periods

This highlights a key lesson:
**Markets are not linear systems**, and simple regression captures trend momentum more than true predictive power.

---

## Possible Extensions

To expand this project:

* Add technical indicators (RSI, MACD)
* Test other stocks or ETFs
* Compare with models like Random Forest or Gradient Boosting
* Predict direction (up/down) instead of exact price
* Turn this into a backtesting strategy

---

## File Structure

```
.
├── main.py
└── README.md
```

---

## Key Takeaway

This project is not about building a profitable trading algorithm.
It is about understanding how machine learning interacts with noisy financial time-series data and why naïve models reveal more about the market’s structure than its future.

---

## License

MIT License
