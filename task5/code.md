1. Problem Statement
Develop a Python program to evaluate multiple mobile recharge plans based on the user's data usage, call minutes, validity period, and budget. The program should calculate excess usage charges when the user exceeds the plan limits, check whether each plan satisfies the given constraints, and identify the most economical eligible mobile plan.
2. Algorithm
1. Start the program.
2. Enter the user's data usage, call minutes, required validity, and budget.
3. Enter the number of mobile plans.
4. For each plan, enter:
   - Plan name
   - Plan cost
   - Data limit
   - Call minutes limit
   - Validity days
5. Calculate excess data charges at ₹10 per GB.
6. Calculate excess call charges at ₹1 per minute.
7. Calculate the total cost of each plan.
8. Check whether the plan satisfies the usage, validity, and budget constraints.
9. If eligible, compare its total cost with other eligible plans.
10. Identify the most economical eligible plan.
11. Display all plan details and the best plan.
12. If no plan is eligible, display a suitable message.
13. Stop the program.

    
3. Flowchart (Mermaid Code)

   <img width="1080" height="1629" alt="image" src="https://github.com/user-attachments/assets/3308f2c4-20fc-4654-a378-0a6417da3344" />


   4. Source Code (Python)
  
      
# Multi-Plan Telecommunications Cost Optimization

# Get User Requirements
data_usage = float(input("Enter required data usage (GB): "))
call_minutes = int(input("Enter required call minutes: "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget: "))

# Validate User Requirements
if data_usage < 0 or call_minutes < 0 or validity <= 0 or budget < 0:
    print("Invalid input! Enter valid requirements.")

else:
    n = int(input("Enter number of mobile plans: "))

    plans = []
    eligible_plans = []

    for i in range(n):
        print("\nEnter Plan", i + 1, "Details")

        name = input("Plan name: ")
        cost = float(input("Plan cost: "))
        data = float(input("Data limit (GB): "))
        calls = int(input("Call minutes limit: "))
        days = int(input("Validity days: "))

        # Validate Plan Details
        if cost < 0 or data < 0 or calls < 0 or days <= 0:
            print("Invalid plan details!")
            continue

        # Calculate Excess Charges
        extra_data = max(0, data_usage - data)
        extra_calls = max(0, call_minutes - calls)

        data_charge = extra_data * 10
        call_charge = extra_calls * 1

        total_cost = cost + data_charge + call_charge

        # Check Eligibility
        eligible = (
            data >= data_usage and
            calls >= call_minutes and
            days >= validity and
            total_cost <= budget
        )

        plans.append((name, total_cost, eligible))

        if eligible:
            eligible_plans.append((name, total_cost))

        print("\nPlan:", name)
        print("Base Cost: Rs.", cost)
        print("Extra Data Charge: Rs.", data_charge)
        print("Extra Call Charge: Rs.", call_charge)
        print("Total Cost: Rs.", total_cost)

        if eligible:
            print("Status: Eligible")
        else:
            print("Status: Not Eligible")

    # Display Best Plan
    print("\n===== PLAN COMPARISON =====")

    if eligible_plans:
        best_plan = min(eligible_plans, key=lambda x: x[1])

        print("Most Economical Plan:", best_plan[0])
        print("Total Cost: Rs.", best_plan[1])

    else:
        print("No eligible mobile plan found.")

    print("\nPlan Evaluation Completed.")

    5. Sample Input



    Enter required data usage (GB): 2
Enter required call minutes: 500
Enter required validity (days): 28
Enter your budget: 300

Enter number of mobile plans: 3

Enter Plan 1 Details
Plan name: Plan A
Plan cost: 199
Data limit (GB): 1.5
Call minutes limit: 400
Validity days: 28

Enter Plan 2 Details
Plan name: Plan B
Plan cost: 249
Data limit (GB): 2.5
Call minutes limit: 600
Validity days: 28

Enter Plan 3 Details
Plan name: Plan C
Plan cost: 299
Data limit (GB): 3
Call minutes limit: 500
Validity days: 56

6. Sample Output

Plan: Plan A
Base Cost: Rs. 199.0
Extra Data Charge: Rs. 5.0
Extra Call Charge: Rs. 100
Total Cost: Rs. 304.0
Status: Not Eligible

Plan: Plan B
Base Cost: Rs. 249.0
Extra Data Charge: Rs. 0
Extra Call Charge: Rs. 0
Total Cost: Rs. 249.0
Status: Eligible

Plan: Plan C
Base Cost: Rs. 299.0
Extra Data Charge: Rs. 0
Extra Call Charge: Rs. 0
Total Cost: Rs. 299.0
Status: Eligible

===== PLAN COMPARISON =====

Most Economical Plan: Plan B
Total Cost: Rs. 249.0

Plan Evaluation Completed.


