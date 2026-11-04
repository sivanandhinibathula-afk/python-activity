
expenses = []

total_expenses = 0

# Enter travel budget
budget = float(input("Enter your travel budget: "))

# Enter base currency
base_currency = input("Enter base currency (INR/USD/EUR): ").upper()

# Enter number of expense categories
n = int(input("Enter number of expense categories: "))

for i in range(n):

    print("\nEnter details of Expense", i + 1)

    category = input("Enter expense category: ")

    amount = float(input("Enter expense amount: "))

    currency = input("Enter currency code: ").upper()

    exchange_rate = float(input("Enter exchange rate: "))

    fee_percent = float(input("Enter conversion fee percentage: "))

    # Convert expense into base currency
    converted_amount = amount * exchange_rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Calculate total expense
    total_amount = converted_amount + conversion_fee

    total_expenses += total_amount

    # Store expense details
    expense = {
        "category": category,
        "amount": amount,
        "currency": currency,
        "converted": converted_amount,
        "fee": conversion_fee,
        "total": total_amount
    }

    expenses.append(expense)


# Identify largest expense category
if expenses:
    largest_expense = max(expenses, key=lambda x: x["total"])
else:
    largest_expense = None

# Calculate budget balance
balance = budget - total_expenses


# Display travel budget report
print("\n========== TRAVEL BUDGET REPORT ==========")

for e in expenses:

    print("\nExpense Category:", e["category"])
    print("Original Amount:", e["amount"], e["currency"])
    print("Converted Amount:", round(e["converted"], 2),
          base_currency)
    print("Conversion Fee: ", round(e["fee"], 2),
          base_currency)
    print("Total Expense:", round(e["total"], 2),
          base_currency)

print("\n---------- FINAL SUMMARY ----------")

print("Travel Budget:", budget, base_currency)

print("Total Travel Expenses:",
      round(total_expenses, 2), base_currency)

if balance >= 0:
    print("Remaining Budget:", round(balance, 2),
          base_currency)
    print("Budget Status: Within Budget")
else:
    print("Budget Excess:", round(abs(balance), 2),
          base_currency)
    print("Budget Status: Budget Exceeded")

if largest_expense:
    print("\nLargest Expense Category:",
          largest_expense["category"])
    print("Largest Expense Amount:",
          round(largest_expense["total"], 2),
          base_currency)

print("\n========== END OF REPORT ==========")

