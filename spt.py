print("Welcome to our Stock Portfolio Tracker")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 200
}

portfolio = {}
total_value = 0

while True:
    stock_symbol = input("\nEnter a stock symbol: ").upper()

    if stock_symbol == "DONE":
        print("\n========== Portfolio Summary ==========")

        with open("portfolio_summary.txt", "w") as file:
            file.write("========== Portfolio Summary ==========\n")

            for symbol, quantity in portfolio.items():
                stock_price = stock_prices[symbol]
                investment_value = stock_price * quantity

                print(f"Stock: {symbol}")
                print(f"Quantity: {quantity}")
                print(f"Price per share: {stock_price}")
                print(f"Investment Value: {investment_value}")
                print("--------------------------------------")

                file.write(f"Stock: {symbol}\n")
                file.write(f"Quantity: {quantity}\n")
                file.write(f"Price per share: {stock_price}\n")
                file.write(f"Investment Value: {investment_value}\n")
                file.write("--------------------------------------\n")

            print(f"Total Portfolio Value: {total_value}")
            file.write(f"Total Portfolio Value: {total_value}\n")

        break
    elif stock_symbol in stock_prices:
        try:
            quantity = int(input("Enter a quantity: "))

            if quantity > 0:
                if stock_symbol in portfolio:
                    portfolio[stock_symbol] += quantity
                else:
                    portfolio[stock_symbol] = quantity

                stock_price = stock_prices[stock_symbol]
                investment_value = stock_price * quantity
                total_value += investment_value

                print(f"\nStock: {stock_symbol}")
                print(f"Quantity: {quantity}")
                print(f"Price per share: {stock_price}")
                print(f"Investment Value: {investment_value}")
            else:
                print("Please enter a quantity greater than 0!")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print("Please enter a valid stock symbol!")