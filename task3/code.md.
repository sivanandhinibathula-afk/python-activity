1. Problem Statement
Develop a Python program to calculate hospital bills by considering consultation charges, diagnostic charges, and treatment charges. The system should apply conditional concessions based on patient category, validate billing constraints, calculate the final payable amount, and classify patients according to their payment status.
2. Algorithm
1. Start the program.
2. Enter patient name and patient category.
3. Enter consultation, diagnostic, and treatment charges.
4. Validate that all charges are non-negative.
5. Calculate the total bill by adding all charges.
6. Apply concessions based on patient category:
   - Senior Citizen – 20% discount.
   - Regular Patient – 10% discount.
   - General Patient – No discount.
7. Calculate the final bill after discount.
8. Enter the amount paid by the patient.
9. Validate that the paid amount is not negative.
10. Calculate the remaining balance.
11. Classify the patient based on payment:
    - Fully Paid – No balance.
    - Partially Paid – Some balance remaining.
    - Unpaid – No payment made.
12. Display the final bill and patient classification.
13. Stop the program.
3. Flowchart
 <img width="1044" height="1599" alt="WhatsApp Image 2026-11-02 at 7 43 41 PM" src="https://github.com/user-attachments/assets/8dcf59e2-fb02-4520-8895-47dcf81e5110" />
 4. Source Code (Python)
 5. 



name = input("Enter patient name: ")

category = input("Enter patient category (Senior/Regular/General): ").lower()

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))


if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
    
    total_bill = consultation + diagnostic + treatment

    
    if category == "senior":
        discount = total_bill * 0.20

    elif category == "regular":
        discount = total_bill * 0.10

    elif category == "general":
        discount = 0

    else:
        discount = -1

    if discount == -1:
        print("Invalid patient category.")

    else:
        
        final_bill = total_bill - discount

        print("\n----- Hospital Bill -----")
        print("Patient Name:", name)
        print("Total Bill: Rs.", total_bill)
        print("Discount: Rs.", discount)
        print("Final Bill: Rs.", final_bill)

        
        paid = float(input("Enter amount paid: "))

        
        if paid < 0 or paid > final_bill:
            print("Invalid payment amount.")

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
5. Sample Input

   
Enter patient name: Ravi
Enter patient category (Senior/Regular/General): senior

Enter consultation charges: 500
Enter diagnostic charges: 1000
Enter treatment charges: 2500

Enter amount paid: 3000
6. Sample Output



----- Hospital Bill -----

Patient Name: Ravi
Total Bill: Rs. 4000.0
Discount: Rs. 800.0
Final Bill: Rs. 3200.0

----- Payment Details -----

Amount Paid: Rs. 3000.0
Remaining Balance: Rs. 200.0
Patient Classification: Partially Paid

Billing Completed Successfully.


