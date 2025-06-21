# main.py
def calculate_portfolio_return(returns, weights):
    portfolio_return = sum(r * w for r, w in zip(returns, weights))
    return round(portfolio_return, 4)

if __name__ == "__main__":
    # Sample data: 5% return, -2% return, 7% return
    returns = [0.06, -0.02, 0.07]
    weights = [0.4, 0.3, 0.3]
    result = calculate_portfolio_return(returns, weights)
    print(f"Your portfolio return is: {result * 100}%")

