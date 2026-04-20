import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

ticker = "PLTR"
data = yf.download(ticker, start="2015-01-01", end="2024-01-01")
data = data[['Close']]
data.head()

data['MA7'] = data['Close'].rolling(window=7).mean()
data['MA30'] = data['Close'].rolling(window=30).mean()
data['Daily_Return'] = data['Close'].pct_change()
data['Volatility'] = data['Daily_Return'].rolling(window=7).std()
data['Target'] = data['Close'].shift(-1)
data.dropna(inplace=True)

X = data[['Close', 'MA7', 'MA30', 'Daily_Return', 'Volatility']]
y = data['Target']

split = int(len(data) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)

latest_features = X.iloc[-1].values.reshape(1, -1)
next_day_prediction = model.predict(latest_features)
print("Predicted next close:", next_day_prediction[0])

plt.figure(figsize=(10,5))
plt.plot(y_test.values, label='Actual')
plt.plot(predictions, label='Predicted')
plt.legend()
plt.show()