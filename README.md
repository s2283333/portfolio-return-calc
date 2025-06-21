# Portfolio Return Calculator

This is a simple Python script that calculates the weighted return of a financial portfolio based on individual asset returns and their weights.

## 🧠 What It Does

The script uses a basic function:

```python
portfolio_return = sum(r * w for r, w in zip(returns, weights))
