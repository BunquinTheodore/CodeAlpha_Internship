import requests
import yfinance as yf
import pandas as pd

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}  # Store stock symbol and the number of shares

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol, shares):
        """Remove a stock from the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}.")
        else:
            print(f"{symbol} not found in portfolio.")

    def get_stock_price(self, symbol):
        """Get the latest stock price using yfinance."""
        try:
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")["Close"].iloc[-1]
            return price
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def track_performance(self):
        """Track portfolio performance."""
        print("\nPortfolio Performance:")
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                value = price * shares
                total_value += value
                print(f"{symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

# Main Program
if __name__ == "__main__":
    tracker = StockPortfolioTracker()
    
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Performance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            tracker.remove_stock(symbol, shares)
        elif choice == "3":
            tracker.track_performance()
        elif choice == "4":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
