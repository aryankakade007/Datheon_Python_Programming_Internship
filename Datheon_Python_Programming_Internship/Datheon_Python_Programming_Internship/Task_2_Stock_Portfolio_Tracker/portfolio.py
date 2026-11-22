import csv
from datetime import datetime


def load_stock_symbols():
    symbols = set()

    try:
        with open("constituents.txt", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row["Symbol"].strip().upper()
                if symbol:
                    symbols.add(symbol)

    except FileNotFoundError:
        print("Error: constituents.txt not found.")

    return symbols


def add_stock(portfolio, valid_symbols):
    symbol = input("Enter stock ticker (e.g., AAPL): ").strip().upper()

    if symbol not in valid_symbols:
        print("Invalid ticker. Please choose a symbol from the S&P 500 dataset.")
        return

    try:
        purchase_price = float(input("Enter purchase price per share ($): "))
        quantity = int(input("Enter quantity of shares: "))
        current_price = float(input("Enter current price per share ($): "))

        if purchase_price <= 0 or current_price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero.")
            return

        portfolio.append({
            "symbol": symbol,
            "purchase_price": purchase_price,
            "quantity": quantity,
            "current_price": current_price
        })

        print(f"{symbol} added to your portfolio.")

    except ValueError:
        print("Please enter valid numeric values.")


def calculate_portfolio(portfolio):
    total_invested = 0
    total_market_value = 0

    for stock in portfolio:
        invested = stock["purchase_price"] * stock["quantity"]
        market_value = stock["current_price"] * stock["quantity"]

        stock["invested"] = invested
        stock["market_value"] = market_value
        stock["gain_loss"] = market_value - invested

        if invested > 0:
            stock["gain_loss_percent"] = (
                stock["gain_loss"] / invested
            ) * 100
        else:
            stock["gain_loss_percent"] = 0

        total_invested += invested
        total_market_value += market_value

    total_gain_loss = total_market_value - total_invested

    if total_invested > 0:
        total_gain_loss_percent = (
            total_gain_loss / total_invested
        ) * 100
    else:
        total_gain_loss_percent = 0

    return (
        total_invested,
        total_market_value,
        total_gain_loss,
        total_gain_loss_percent
    )


def display_portfolio(portfolio, totals):
    (
        total_invested,
        total_market_value,
        total_gain_loss,
        total_gain_loss_percent
    ) = totals

    print("\n" + "=" * 75)
    print("                 STOCK PORTFOLIO SUMMARY")
    print("=" * 75)

    if not portfolio:
        print("Your portfolio is empty.")
        return

    print(
        f"{'Ticker':<10}{'Quantity':<10}{'Invested ($)':<16}"
        f"{'Market Value ($)':<19}{'Gain/Loss ($)':<15}"
    )
    print("-" * 75)

    for stock in portfolio:
        print(
            f"{stock['symbol']:<10}"
            f"{stock['quantity']:<10}"
            f"{stock['invested']:<16.2f}"
            f"{stock['market_value']:<19.2f}"
            f"{stock['gain_loss']:<15.2f}"
        )

    print("-" * 75)
    print(f"Total Invested:       ${total_invested:.2f}")
    print(f"Current Market Value: ${total_market_value:.2f}")
    print(f"Total Gain/Loss:      ${total_gain_loss:.2f}")
    print(f"Gain/Loss Percentage: {total_gain_loss_percent:.2f}%")
    print("=" * 75)


def save_portfolio_log(portfolio, totals):
    (
        total_invested,
        total_market_value,
        total_gain_loss,
        total_gain_loss_percent
    ) = totals

    file_exists = False

    try:
        with open("portfolio_summary.csv", "r", newline="", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open("portfolio_summary.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date and Time",
                "Ticker",
                "Quantity",
                "Purchase Price",
                "Current Price",
                "Invested",
                "Market Value",
                "Gain/Loss",
                "Gain/Loss %",
                "Portfolio Total Invested",
                "Portfolio Total Market Value",
                "Portfolio Total Gain/Loss",
                "Portfolio Total Gain/Loss %"
            ])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for stock in portfolio:
            writer.writerow([
                timestamp,
                stock["symbol"],
                stock["quantity"],
                stock["purchase_price"],
                stock["current_price"],
                stock["invested"],
                stock["market_value"],
                stock["gain_loss"],
                stock["gain_loss_percent"],
                total_invested,
                total_market_value,
                total_gain_loss,
                total_gain_loss_percent
            ])

    print("Portfolio log saved to portfolio_summary.csv")


def main():
    portfolio = []
    valid_symbols = load_stock_symbols()

    if not valid_symbols:
        print("No stock symbols loaded. Please check constituents.txt.")
        return

    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add stock")
        print("2. View portfolio summary")
        print("3. Save portfolio summary to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_stock(portfolio, valid_symbols)

        elif choice == "2":
            totals = calculate_portfolio(portfolio)
            display_portfolio(portfolio, totals)

        elif choice == "3":
            totals = calculate_portfolio(portfolio)
            display_portfolio(portfolio, totals)
            save_portfolio_log(portfolio, totals)

        elif choice == "4":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()