months = []
bills = []

n = int(input("Enter number of months: "))

fixed_charge = 50
surcharge_rate = 0.05
rebate_rate = 0.05

for i in range(n):

    print("\nEnter details for Month", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charges
    fixed = fixed_charge

    # Surcharge calculation
    surcharge = energy_charge * surcharge_rate

    # Rebate calculation
    if units < 100:
        rebate = energy_charge * rebate_rate
    else:
        rebate = 0

    # Final bill
    total_bill = energy_charge + fixed + surcharge - rebate

    months.append(month)
    bills.append(total_bill)

    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total_bill, 2))


# Monthly bill comparison
print("\n========== MONTHLY BILL COMPARISON ==========")

for i in range(n):
    print(months[i], "Bill: Rs.", round(bills[i], 2))

print("\n========== UNUSUAL BILL INCREASES ==========")

found = False

for i in range(1, n):

    previous_bill = bills[i - 1]
    current_bill = bills[i]

    if current_bill > previous_bill:
        increase = current_bill - previous_bill
        percentage = (increase / previous_bill) * 100

        if percentage > 30:
            print(months[i], "- Unusual increase detected")
            print("Increase: Rs.", round(increase, 2))
            print("Increase Percentage:", round(percentage, 2), "%")
            found = True

if not found:
    print("No unusual increases detected.")
