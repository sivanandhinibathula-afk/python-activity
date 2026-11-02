



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
        deduction = 500 + (gross - 20000) * 0.10

    else:
        deduction = 500 + 2000 + (gross - 40000) * 0.15

    
    net_salary = gross - deduction

    
    print("\n===== SALARY STATEMENT =====")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowances)
    print("Overtime: Rs.", overtime)
    print("Incentives: Rs.", incentives)
    print("----------------------------")
    print("Gross Salary: Rs.", gross)
    print("Total Deductions: Rs.", deduction)
    print("Net Salary: Rs.", net_salary)
    print("============================")
    print("Payroll Completed Successfully")

