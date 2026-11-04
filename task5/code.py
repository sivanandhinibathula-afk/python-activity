plans = []
eligible_plans = []

# Enter user requirements
data_required = float(input("Enter required data in GB: "))
calls_required = float(input("Enter required call minutes: "))
validity_required = int(input("Enter required validity in days: "))
budget = float(input("Enter maximum budget: "))

n = int(input("\nEnter number of mobile plans: "))

for i in range(n):

    print("\nEnter details of Plan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter included data in GB: "))
    calls = float(input("Enter included call minutes: "))
    validity = int(input("Enter validity in days: "))

    data_rate = float(input("Enter excess data charge per GB: "))
    call_rate = float(input("Enter excess call charge per minute: "))

    # Validate inputs
    if (price < 0 or data < 0 or calls < 0
            or validity < 0 or data_rate < 0 or call_rate < 0):
        print("Invalid plan details!")
        continue

    # Calculate excess usage
    excess_data = max(0, data_required - data)
    excess_calls = max(0, calls_required - calls)

    # Calculate additional charges
    data_charge = excess_data * data_rate
    call_charge = excess_calls * call_rate

    # Calculate total cost
    total_cost = price + data_charge + call_charge

    # Check eligibility
    if (data >= data_required
            and calls >= calls_required
            and validity >= validity_required
            and total_cost <= budget):

        status = "Eligible"

        eligible_plans.append({
            "name": name,
            "price": price,
            "data": data,
            "calls": calls,
            "validity": validity,
            "excess_data": excess_data,
            "excess_calls": excess_calls,
            "data_charge": data_charge,
            "call_charge": call_charge,
            "total_cost": total_cost
        })

    else:
        status = "Not Eligible"

    plans.append({
        "name": name,
        "excess_data": excess_data,
        "excess_calls": excess_calls,
        "data_charge": data_charge,
        "call_charge": call_charge,
        "total_cost": total_cost,
        "status": status
    })


# Display all plan details
print("\n========== MOBILE PLAN COMPARISON ==========")

for plan in plans:

    print("\nPlan Name:", plan["name"])
    print("Excess Data:", plan["excess_data"], "GB")
    print("Excess Calls:", plan["excess_calls"], "minutes")
    print("Data Charges: Rs.", round(plan["data_charge"], 2))
    print("Call Charges: Rs.", round(plan["call_charge"], 2))
    print("Total Cost: Rs.", round(plan["total_cost"], 2))
    print("Status:", plan["status"])


# Find most economical eligible plan
print("\n========== BEST MOBILE PLAN ==========")

if eligible_plans:

    best_plan = min(
        eligible_plans,
        key=lambda x: x["total_cost"]
    )

    print("Most Economical Plan:", best_plan["name"])
    print("Plan Price: Rs.", best_plan["price"])
    print("Total Cost: Rs.", round(best_plan["total_cost"], 2))
    print("Included Data:", best_plan["data"], "GB")
    print("Included Calls:", best_plan["calls"], "minutes")
    print("Validity:", best_plan["validity"], "days")

else:
    print("No eligible mobile plan found.")
