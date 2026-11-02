
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))


consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))


if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
    
    total = consultation + diagnostic + treatment

    
    if age >= 60:
        discount = total * 0.20
    elif age < 18:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("\n----- Hospital Bill -----")
    print("Patient Name:", name)
    print("Total Charges: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final_bill)

    
    paid = float(input("Enter amount paid: "))

    
    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")

    else:
        balance = final_bill - paid

        
        if balance == 0:
            status = "Fully Paid"
        elif paid > 0:
            status = "Partially Paid"
        else:
            status = "Unpaid"

        
        print("\n----- Payment Details -----")
        print("Amount Paid: Rs.", paid)
        print("Remaining Balance: Rs.", balance)
        print("Patient Classification:", status)

        print("Billing Completed Successfully.")

