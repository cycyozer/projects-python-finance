prices = [100, 102, 101, 105, 107, 104]

returns = [prices[i] / prices[i - 1] - 1 for i in range(1, len(prices))]
cumulative_return = prices[-1] / prices[0] - 1

mean_return = sum(returns) / len(returns)
variance = sum((r - mean_return) ** 2 for r in returns) / (len(returns) - 1)
volatility = variance ** 0.5

print(f"Cumulative return: {cumulative_return:.2%}")
print(f"Volatility per period: {volatility:.2%}")