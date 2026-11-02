1. Problem Statement
Develop a Python program to calculate employee salary based on basic pay, allowances, overtime, and incentives. The system should calculate gross salary, apply progressive deductions based on salary slabs, calculate net salary, and generate a formatted salary statement.
2. Algorithm
1. Start the program.
2. Enter employee name and ID.
3. Enter basic salary, allowances, overtime, and incentives.
4. Validate that all salary values are non-negative.
5. Calculate gross salary by adding basic pay, allowances, overtime, and incentives.
6. Calculate deductions using progressive salary slabs:
   - First ₹10,000 – 0% deduction.
   - Next ₹10,000 – 5% deduction.
   - Next ₹20,000 – 10% deduction.
   - Above ₹40,000 – 15% deduction.
7. Calculate total deductions.
8. Calculate net salary by subtracting deductions from gross salary.
9. Display the formatted salary statement.
10. Stop the program.
11. 
3. Flowchart

   <img width="1080" height="1577" alt="image" src="https://github.com/user-attachments/assets/989ff4d7-a3b2-4d9e-a61a-eaa6b064d68c" />

   
4. Source Code (Python)


name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")


basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))


if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid salary details!")

else:
    
    gross = basic + allowances + overtime + incentives

    
    if gross <= 10000:
        deduction = 0

    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05

    elif gross <= 40000:
        deduction = (10000 * 0.05) + (gross - 20000) * 0.10

    else:
        deduction = (10000 * 0.05) + (20000 * 0.10) + (gross - 40000) * 0.15

    
    net_salary = gross - deduction

    
    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("--------------------------------------")
    print("Basic Salary  : Rs.", round(basic, 2))
    print("Allowances    : Rs.", round(allowances, 2))
    print("Overtime      : Rs.", round(overtime, 2))
    print("Incentives    : Rs.", round(incentives, 2))
    print("--------------------------------------")
    print("Gross Salary  : Rs.", round(gross, 2))
    print("Deductions    : Rs.", round(deduction, 2))
    print("Net Salary    : Rs.", round(net_salary, 2))
    print("======================================")
    print("Payroll Process Completed Successfully.")


    5. Sample Input


    Enter employee name: Ravi
Enter employee ID: 101

Enter basic salary: 25000
Enter allowances: 5000
Enter overtime amount: 3000
Enter incentives: 2000

6. Sample Output

7. ========== SALARY STATEMENT ==========

Employee Name : Ravi
Employee ID   : 101
--------------------------------------
Basic Salary  : Rs. 25000.0
Allowances    : Rs. 5000.0
Overtime      : Rs. 3000.0
Incentives    : Rs. 2000.0
--------------------------------------
Gross Salary  : Rs. 35000.0
Deductions    : Rs. 2000.0
Net Salary    : Rs. 33000.0
======================================
Payroll Process Completed Successfully.




