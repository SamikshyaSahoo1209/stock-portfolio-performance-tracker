
import csv

# Store portfolio details
portfolio = {}

# Function to add stocks
def add_stock():
    symbol = input("Enter stock ticker symbol: ").upper()
    purchase_price = float(input("Enter purchase price: "))
    quantity = int(input("Enter quantity: "))

    portfolio[symbol] = {
        "purchase_price": purchase_price,
        "quantity": quantity
    }

    print("Stock added successfully!\n")


# Read current stock prices from CSV
def load_stock_prices(filename):
    stock_prices = {}

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row.get("Symbol") or row.get("symbol")
                price = row.get("Price") or row.get("price")

                if symbol and price:
                    stock_prices[symbol.upper()] = float(price)

    except FileNotFoundError:
        print("CSV file not found!")

    return stock_prices


# Calculate portfolio performance
def calculate_performance(stock_prices):
    total_investment = 0
    total_value = 0

    print("\n----- STOCK PORTFOLIO SUMMARY -----")

    for symbol, details in portfolio.items():

        purchase_price = details["purchase_price"]
        quantity = details["quantity"]

        current_price = stock_prices.get(symbol)

        if current_price is None:
            print(f"{symbol}: Current price unavailable")
            continue

        investment = purchase_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - investment

        percentage = (profit_loss / investment) * 100

        total_investment += investment
        total_value += current_value

        print("\nStock:", symbol)
        print("Investment:", investment)
        print("Current Value:", current_value)
        print("Profit/Loss:", profit_loss)
        print("Gain/Loss Percentage:", round(percentage, 2), "%")

    total_profit = total_value - total_investment

    print("\nTotal Investment:", total_investment)
    print("Total Current Value:", total_value)
    print("Total Profit/Loss:", total_profit)


# Export results to CSV
def export_summary(stock_prices):
    with open("portfolio_summary.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Symbol",
            "Purchase Price",
            "Quantity",
            "Current Price",
            "Investment",
            "Current Value",
            "Profit/Loss",
            "Gain/Loss Percentage"
        ])

        for symbol, details in portfolio.items():

            current_price = stock_prices.get(symbol)

            if current_price is None:
                continue

            purchase = details["purchase_price"]
            quantity = details["quantity"]

            investment = purchase * quantity
            value = current_price * quantity
            profit = value - investment
            percentage = (profit / investment) * 100

            writer.writerow([
                symbol,
                purchase,
                quantity,
                current_price,
                investment,
                value,
                profit,
                round(percentage, 2)
            ])

    print("\nCSV report generated successfully!")


# Main program
def main():

    filename = input("Enter CSV filename: ")
    stock_prices = load_stock_prices(filename)

    while True:

        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add Stock")
        print("2. View Performance")
        print("3. Export CSV Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()

        elif choice == "2":
            calculate_performance(stock_prices)

        elif choice == "3":
            export_summary(stock_prices)

        elif choice == "4":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
