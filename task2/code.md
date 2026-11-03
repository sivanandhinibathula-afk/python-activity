1. Problem Statement
Develop a Python program to calculate household electricity bills based on multiple consumption slabs. The system should calculate electricity charges according to units consumed, add fixed charges and surcharges, apply rebates if applicable, compare electricity bills across several months, and identify unusual increases in monthly bills.





2. Algorithm



1. Start the program.
2. Read the number of months.
3. Enter the electricity units consumed for each month.
4. Calculate the electricity charges using progressive slabs:
   - First 100 units – ₹2 per unit.
   - Next 100 units – ₹3 per unit.
   - Next 100 units – ₹5 per unit.
   - Above 300 units – ₹7 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge on the energy charges.
7. Apply a 10% rebate if consumption is below 100 units.
8. Calculate the final electricity bill.
9. Compare bills of different months.
10. Identify unusual increases if the current bill increases by more than 30% compared to the previous month.
11. Display monthly bills and unusual increases.
12. Stop the program.
3. Flowchart

. <img width="1046" height="1600" alt="WhatsApp Image 2026-11-02 at 7 26 47 PM" src="https://github.com/user-attachments/assets/c9059211-6e09-4fb7-937f-e9dc4904f3d8" />


4. Source Code (Python)





def calculate_bill(units):

    # Calculate charges based on electricity slabs
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed_charge = 50

    surcharge = energy_charge * 0.05

    # Apply rebate for consumption below 100 units
    if units < 100:
        rebate = energy_charge * 0.10
    else:
        rebate = 0

    total_bill = energy_charge + fixed_charge + surcharge - rebate

    return total_bill


5.SOURCE  CODE


n = int(input("Enter number of months: "))

bills = []

for i in range(n):

    print("\nMonth", i + 1)

    units = int(input("Enter electricity units consumed: "))

    bill = calculate_bill(units)

    bills.append(bill)

    print("Electricity Bill: Rs.", round(bill, 2))


# Compare monthly bills
print("\n----- Monthly Bill Comparison -----")

for i in range(n):

    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0:

        increase = bills[i] - bills[i - 1]

        percentage = (increase / bills[i - 1]) * 100

        if percentage > 30:
            print("Warning: Unusual increase detected!")

        else:
            print("Normal Bill Increase/Change.")

print("\nBilling Process Completed.")
5. SOURCE  Output
Enter number of months: 4

Month 1
Enter electricity units consumed: 80
Electricity Bill: Rs. 201.2

Month 2
Enter electricity units consumed: 120
Electricity Bill: Rs. 312.5

Month 3
Enter electricity units consumed: 150
Electricity Bill: Rs. 407.5

Month 4
Enter electricity units consumed: 300
Electricity Bill: Rs. 1032.5

----- Monthly Bill Comparison -----

Month 1 Bill: Rs. 201.2

Month 2 Bill: Rs. 312.5
Warning: Unusual increase detected!

Month 3 Bill: Rs. 407.5
Normal Bill Increase/Change.

Month 4 Bill: Rs. 1032.5
Warning: Unusual increase detected!

Billing Process Completed.



