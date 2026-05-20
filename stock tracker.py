# Predefined stock prices
stock_prices = {
    "APPLES": 180,
    "MANGOES": 250,
    "ORANGES": 140,
    "GUAVA": 330,
    "WATERMELON": 145
}

# Store user portfolio
portfolio = {}

# Store total investment value
total_investment = 0

print("\n STOCK PORTFOLIO TRACKER \n")

while True:

    # Take stock symbol input
    stock_name = input(
        "Enter Stock Symbol (APPLES ,MANGOES ,ORANGES ,GUAVA ,WATERMELON): "
    ).upper()

    # Validate stock symbol
    if stock_name not in stock_prices:
        print(" Stock not available. Please try again.\n")
        continue

    # Quantity input with validation
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print(" Quantity must be greater than 0.\n")
            continue

    except ValueError:
        print(" Invalid input. Please enter a valid number.\n")
        continue

    # Calculate investment
    investment = stock_prices[stock_name] * quantity

    # Save stock details
    portfolio[stock_name] = {
        "quantity": quantity,
        "price": stock_prices[stock_name],
        "investment": investment
    }

    # Add to total investment
    total_investment += investment

    print(f" {stock_name} added successfully!\n")

    # Ask user to continue
    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

# Display portfolio summary
print("\n PORTFOLIO SUMMARY \n")

for stock, details in portfolio.items():

    print(f"Stock Name   : {stock}")
    print(f"Stock Price  : ${details['price']}")
    print(f"Quantity     : {details['quantity']}")
    print(f"Investment   : ${details['investment']}")
    print("-----------------------------------")

print(f"\n Total Investment Value: ${total_investment}")

# Save report to text file
with open("portfolio_summary.txt", "w") as file:

    file.write("========== PORTFOLIO SUMMARY ==========\n\n")

    for stock, details in portfolio.items():

        file.write(f"Stock Name   : {stock}\n")
        file.write(f"Stock Price  : ${details['price']}\n")
        file.write(f"Quantity     : {details['quantity']}\n")
        file.write(f"Investment   : ${details['investment']}\n")
        file.write("-----------------------------------\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n Portfolio summary saved in 'portfolio_summary.txt'")
print("\n PROGRAM FINISHED ")