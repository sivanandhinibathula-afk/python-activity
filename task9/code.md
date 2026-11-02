1. Problem Statement
Develop a Python program to analyze a travel budget by converting expenses from different currencies into a base currency using supplied exchange rates. The program calculates conversion fees, total travel expenses, and compares the total spending against the planned budget. It also identifies the largest expense category and displays whether the travel expenses are within or exceed the budget.
3. Algorithm
1. Start the program.
2. Enter the base currency.
3. Enter the number of expense categories.
4. For each expense, enter the category name.
5. Enter the expense amount and currency.
6. Enter the exchange rate for that currency.
7. Convert the expense into the base currency.
8. Calculate the conversion fee.
9. Add the converted amount and fee to the total expe
10.
11. nses.
12. Store each category's total expense.
13. Repeat until all expenses are entered.
14. Enter the planned travel budget.
15. Calculate the total travel expenditure.
16. Identify the largest expense category.
17. Compare total expenditure with the planned budget.
18. Display the travel budget report.
19. Stop the program.
3. Flowchart – Mermaid Code




<img width="1080" height="1570" alt="image" src="https://github.com/user-attachments/assets/858c9e30-a842-43b6-b599-5e8c9296d933" />

4. Source Code (Python)

   
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

    # Calculate expense including fee
    final_amount = converted_amount + fee

    expenses[category] = final_amount

    total_expenses += final_amount
    total_fees += fee

# Enter planned budget
budget = float(input("\nEnter planned travel budget: "))

# Find largest expense category
largest_category = max(expenses, key=expenses.get)

largest_amount = expenses[largest_category]

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display report
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


5. Source Input

   Enter base currency (INR/USD/EUR): INR
Enter number of expense categories: 3

Enter expense details 1
Enter expense category: Hotel
Enter expense amount: 100
Enter currency code: USD
Enter exchange rate: 85

Enter expense details 2
Enter expense category: Food
Enter expense amount: 50
Enter currency code: USD
Enter exchange rate: 85

Enter expense details 3
Enter expense category: Shopping
Enter expense amount: 100
Enter currency code: EUR
Enter exchange rate: 95

Enter planned travel budget: 25000

6. Source Output

===== TRAVEL BUDGET REPORT =====

Hotel : 8670.0 INR
Food : 4335.0 INR
Shopping : 9690.0 INR

--------------------------------
Total Conversion Fees: 445.0
Total Travel Expenses: 22695.0
Planned Budget: 25000.0
Largest Expense Category: Shopping
Largest Expense Amount: 9690.0

Status: Travel is within budget
Remaining Budget: 2305.0

================================
