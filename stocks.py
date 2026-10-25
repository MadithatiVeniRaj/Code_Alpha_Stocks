
stock_prices = {
    "AAPL": 333.69,
    "TSLA": 370.59,
    "GOOGL": 343.50,
    "MSFT": 517.53,
    "AMZN": 251.52,
    "LLY":1142.85,
    "META":728.08,
    "AVGO":355.14,
    "NVDA":233.95,
    "NFLX":67.06
}


def show_available_stocks():
    print("\nAvailable stocks and their prices:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol:<6} ${price}")


def get_quantity(symbol):

    while True:
        qty_input = input(f"Enter quantity of {symbol}: ").strip()
        try:
            quantity = float(qty_input)
            if quantity <= 0:
                print("Quantity must be greater than zero. Try again.")
                continue
            return quantity
        except ValueError:
            print("That's not a valid number. Please enter digits only.")


def build_portfolio():

    portfolio = {}
    show_available_stocks()

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print(f"'{symbol}' isn't in our price list. Please choose from the list above.")
            continue

        quantity = get_quantity(symbol)


        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_total(portfolio):

    breakdown = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = price * quantity
        breakdown.append((symbol, quantity, price, value))
        total += value

    return breakdown, total


def print_summary(breakdown, total):
    print("\n" + "=" * 40)
    print("PORTFOLIO SUMMARY")
    print("=" * 40)

    if not breakdown:
        print("No stocks were added.")
        return

    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<6} {quantity:>6} shares x ${price:<6} = ${value:,.2f}")

    print("-" * 40)
    print(f"{'TOTAL INVESTMENT':<28} ${total:,.2f}")
    print("=" * 40)


def save_to_file(breakdown, total):

    choice = input("\nSave this summary to a file? (y/n): ").strip().lower()
    if choice != "y":
        print("Okay, not saving. Goodbye!")
        return

    filename = input("Enter filename (e.g. portfolio.txt): ").strip()
    if not filename:
        filename = "portfolio.txt"

    try:
        with open(filename, "w") as file:
            file.write("PORTFOLIO SUMMARY\n")
            file.write("=" * 40 + "\n")

            for symbol, quantity, price, value in breakdown:
                file.write(f"{symbol:<6} {quantity:>6} shares x ${price:<6} = ${value:,.2f}\n")

            file.write("-" * 40 + "\n")
            file.write(f"TOTAL INVESTMENT: ${total:,.2f}\n")

        print(f"Saved! Check the file '{filename}' in your project folder.")
    except OSError as error:
        print(f"Sorry, couldn't save the file: {error}")


def main():
    print("Welcome to the Stock Portfolio Tracker!")
    portfolio = build_portfolio()
    breakdown, total = calculate_total(portfolio)
    print_summary(breakdown, total)

    if breakdown:
        save_to_file(breakdown, total)


if __name__ == "__main__":
    main()