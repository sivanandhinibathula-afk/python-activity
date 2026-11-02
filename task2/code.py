


def calculate_bill(units):

    
    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed_charge = 50
    surcharge = charge * 0.05

    if units < 100:
        rebate = charge * 0.10
    else:
        rebate = 0

    total = charge + fixed_charge + surcharge - rebate

    return total




n = int(input("Enter number of months: "))

bills = []

for i in range(n):
    print("\nMonth", i + 1)

    units = int(input("Enter units consumed: "))

    bill = calculate_bill(units)

    bills.append(bill)

    print("Total Electricity Bill: Rs.", round(bill, 2))




print("\nMonthly Bill Comparison")

for i in range(n):

    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        percentage = (increase / bills[i - 1]) * 100

        if percentage > 30:
            print("Unusual Increase Detected!")

        else:
            print("Normal Bill Change.")

print("\nBilling Completed Successfully.")

