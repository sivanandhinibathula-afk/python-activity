patients = []

n = int(input("Enter number of patients: "))

for i in range(n):

    print("\nEnter details of Patient", i + 1)

    name = input("Enter patient name: ")

    age = int(input("Enter patient age: "))

    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))

    print("\nPatient Categories:")
    print("1. Senior Citizen")
    print("2. Below Poverty Line")
    print("3. Regular")

    category = int(input("Enter patient category (1-3): "))

    # Validate patient details
    if (age <= 0 or consultation < 0
            or diagnostic < 0 or treatment < 0
            or category not in [1, 2, 3]):
        print("Invalid patient details. Skipping patient.")
        continue

    # Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Apply concessions
    if category == 1:
        concession_rate = 0.10
        category_name = "Senior Citizen"

    elif category == 2:
        concession_rate = 0.20
        category_name = "Below Poverty Line"

    else:
        concession_rate = 0
        category_name = "Regular"

    concession = total_bill * concession_rate

    final_bill = total_bill - concession

    # Validate payment
    payment = float(input("Enter amount paid: "))

    while payment < 0 or payment > final_bill:
        print("Invalid payment! Enter amount between 0 and", final_bill)
        payment = float(input("Re-enter payment amount: "))

    # Calculate balance
    balance = final_bill - payment

    # Patient classification
    if payment == final_bill:
        status = "Fully Paid"

    elif payment > 0:
        status = "Partially Paid"

    else:
        status = "Unpaid"

    # Store patient details
    patients.append({
        "name": name,
        "age": age,
        "category": category_name,
        "total": total_bill,
        "concession": concession,
        "final": final_bill,
        "payment": payment,
        "balance": balance,
        "status": status
    })

# Display billing report
print("\n========== HOSPITAL BILLING REPORT ==========")

for patient in patients:

    print("\nPatient Name:", patient["name"])
    print("Age:", patient["age"])
    print("Category:", patient["category"])
    print("Total Bill: Rs.", round(patient["total"], 2))
    print("Concession: Rs.", round(patient["concession"], 2))
    print("Final Bill: Rs.", round(patient["final"], 2))
    print("Amount Paid: Rs.", round(patient["payment"], 2))
    print("Balance Amount: Rs.", round(patient["balance"], 2))
    print("Payment Classification:", patient["status"])

print("\nTotal Patients Processed:", len(patients))
