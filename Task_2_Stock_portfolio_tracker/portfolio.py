import csv
import os

# Get the location of the CSV file
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "stock_prices.csv")

# Load stock symbols
stock_data = {}

with open(file_path, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stock_data[row["Symbol"].upper()] = row["Security"]

# Store portfolio details
portfolio = []

print("=" * 50)
print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 50)

while True:

    symbol = input("\nEnter stock ticker symbol: ").upper()

    if symbol not in stock_data:
        print("Invalid stock symbol! Try again.")
        continue

    print("Company Name:", stock_data[symbol])

    try:
        purchase_price = float(input("Enter purchase price: "))
        shares = int(input("Enter number of shares: "))
        current_price = float(input("Enter current price: "))

        if purchase_price <= 0 or current_price < 0 or shares <= 0:
            print("Please enter valid values.")
            continue

    except ValueError:
        print("Invalid input! Enter numeric values.")
        continue

    investment = purchase_price * shares
    current_value = current_price * shares

    profit_loss = current_value - investment
    percentage = (profit_loss / investment) * 100

    portfolio.append({
        "Symbol": symbol,
        "Company": stock_data[symbol],
        "Investment": investment,
        "Current Value": current_value,
        "Profit/Loss": profit_loss,
        "Percentage": percentage
    })

    choice = input("\nAdd another stock? (yes/no): ")

    if choice.lower() != "yes":
        break

# Display portfolio report

print("\n" + "=" * 50)
print("              PORTFOLIO SUMMARY")
print("=" * 50)

total_investment = 0
total_value = 0

for stock in portfolio:

    print("\nStock:", stock["Symbol"])
    print("Company:", stock["Company"])
    print("Investment: $", round(stock["Investment"], 2))
    print("Current Value: $", round(stock["Current Value"], 2))
    print("Profit/Loss: $", round(stock["Profit/Loss"], 2))
    print("Percentage:", round(stock["Percentage"], 2), "%")

    total_investment += stock["Investment"]
    total_value += stock["Current Value"]

total_profit = total_value - total_investment

print("\n" + "-" * 50)
print("Total Investment: $", round(total_investment, 2))
print("Current Portfolio Value: $", round(total_value, 2))
print("Total Profit/Loss: $", round(total_profit, 2))

if total_investment > 0:
    overall_percentage = (total_profit / total_investment) * 100
    print("Overall Gain/Loss:", round(overall_percentage, 2), "%")

print("=" * 50)
print("       PORTFOLIO CALCULATION COMPLETED!")
print("=" * 50)

# Save portfolio results into CSV file

output_file = os.path.join(folder_path, "portfolio_summary.csv")

with open(output_file, "w", newline="") as file:

    fieldnames = [
        "Symbol",
        "Company",
        "Investment",
        "Current Value",
        "Profit/Loss",
        "Percentage"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for stock in portfolio:
        writer.writerow(stock)

print("\nPortfolio report saved successfully!")