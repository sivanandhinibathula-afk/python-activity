
# Multi-Currency Travel Budget Analysis

base_currency = input("Enter base currency (INR/USD/EUR): ").upper()

n = int(input("Enter number of expense categories: "))

expenses = {}
total_expenses = 0
total_fees = 0

for i in range(n):
    print("\nEnter expense details", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code: ").upper()
    exchange_rate = float(input("Enter exchange rate: "))

    # Convert expense into base currency
    converted_amount = amount * exchange_rate

    # Calculate conversion fee (2%)
    fee = converted_amount * 2 / 100

    # Calculate total expense
    final_amount = converted_amount + fee

    expenses[category] = final_amount

    total_expenses += final_amount
    total_fees += fee

# Enter planned budget
budget = float(input("\nEnter planned travel budget: "))

# Identify largest expense category
largest_category = max(expenses, key=expenses.get)
largest_amount = expenses[largest_category]

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display travel budget report
print("\n===== TRAVEL BUDGET REPORT =====")

for category, amount in expenses.items():
    print(category, ":", round(amount, 2), base_currency)

print("--------------------------------")
print("Total Conversion Fees:", round(total_fees, 2))
print("Total Travel Expenses:", round(total_expenses, 2))
print("Planned Budget:", round(budget, 2))
print("Largest Expense Category:", largest_category)
print("Largest Expense Amount:", round(largest_amount, 2))

if total_expenses <= budget:
    print("Status: Travel is within budget")
    print("Remaining Budget:", round(remaining_budget, 2))
else:
    print("Status: Travel budget exceeded")
    print("Extra Amount Required:", round(abs(remaining_budget), 2))

print("================================")

