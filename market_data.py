import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["SAP.DE", "ASML.AS", "MC.PA"]
prices = yf.download(tickers, start="2023-01-01", auto_adjust=True)["Close"]

returns = prices.pct_change().dropna()
cumulative = (1 + returns).cumprod() - 1
annual_volatility = returns.std() * 252 ** 0.5

print(annual_volatility)
cumulative.plot(title="Cumulative return")

plt.show()
