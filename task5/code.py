
data_usage = float(input("Enter required data usage (GB): "))
call_minutes = int(input("Enter required call minutes: "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget: "))

if data_usage < 0 or call_minutes < 0 or validity <= 0 or budget < 0:
    print("Invalid input!")

else:
    n = int(input("Enter number of mobile plans: "))

    eligible_plans = []

    for i in range(n):
        print("\nEnter Plan", i + 1, "Details")

        name = input("Enter plan name: ")
        cost = float(input("Enter plan cost: "))
        data = float(input("Enter data limit (GB): "))
        calls = int(input("Enter call minutes: "))
        days = int(input("Enter validity days: "))

        if cost < 0 or data < 0 or calls < 0 or days <= 0:
            print("Invalid plan details!")
            continue

        
        extra_data = max(0, data_usage - data)
        extra_calls = max(0, call_minutes - calls)

        data_charge = extra_data * 10
        call_charge = extra_calls * 1

        total_cost = cost + data_charge + call_charge

    
        if (data >= data_usage and
            calls >= call_minutes and
            days >= validity and
            total_cost <= budget):

            print("Plan Status: Eligible")
            eligible_plans.append((name, total_cost))

        else:
            print("Plan Status: Not Eligible")

        print("Extra Data Charge: Rs.", data_charge)
        print("Extra Call Charge: Rs.", call_charge)
        print("Total Cost: Rs.", total_cost)

    
    print("\n----- PLAN COMPARISON -----")

    if eligible_plans:
        best_plan = min(eligible_plans, key=lambda x: x[1])

        print("Most Economical Plan:", best_plan[0])
        print("Total Cost: Rs.", best_plan[1])

    else:
        print("No Eligible Mobile Plan Found")

    print("\nPlan Evaluation Completed Successfully.")
