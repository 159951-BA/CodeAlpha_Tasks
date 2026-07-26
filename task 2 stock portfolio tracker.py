# Stock prices hardcoded
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 200,
    "NVDA": 880,
    "META": 500,
    "NFLX": 650
}

portfolio = []

print("=== STOCK PORTFOLIO TRACKER ===")
print()
print("Available stocks:")
for stock in stock_prices:
    print(stock, "= $", stock_prices[stock])

while True:
    print()
    stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Try again.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    total = price * quantity

    portfolio.append([stock_name, price, quantity, total])
    print("Added", quantity, "shares of", stock_name)

print()
print("=== PORTFOLIO SUMMARY ===")

grand_total = 0

for item in portfolio:
    print(item[0], "- $", item[1], "x", item[2], "= $", item[3])
    grand_total = grand_total + item[3]

print("Total investment: $", grand_total)

save = input("Save to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("STOCK PORTFOLIO\n")
    for item in portfolio:
        file.write(item[0] + " - " + str(item[2]) + " shares = $" + str(item[3]) + "\n")
    file.write("Total: $" + str(grand_total) + "\n")
    file.close()
    print("Saved to portfolio.txt")