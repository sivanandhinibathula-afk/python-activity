employees = []

n = int(input("Enter number of employees: "))

for i in range(n):

    print("\nEnter Employee Details", i + 1)

    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")

    basic = float(input("Enter basic pay: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    overtime_hours = float(input("Enter overtime hours: "))
    overtime_rate = float(input("Enter overtime rate per hour: "))
    incentives = float(input("Enter incentives: "))

    # Input validation
    if (basic < 0 or hra < 0 or da < 0
            or overtime_hours < 0
            or overtime_rate < 0 or incentives < 0):

        print("Invalid salary details!")
        continue

    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = basic + hra + da + overtime_pay + incentives

    # Progressive deduction calculation
    if gross_salary <= 10000:
        deduction = 0

    elif gross_salary <= 20000:
        deduction = (gross_salary - 10000) * 0.05

    elif gross_salary <= 40000:
        deduction = (10000 * 0.05) + (gross_salary - 20000) * 0.10

    else:
        deduction = (10000 * 0.05) + (20000 * 0.10) + (gross_salary - 40000) * 0.15

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Store employee details
    employees.append({
        "id": emp_id,
        "name": name,
        "basic": basic,
        "hra": hra,
        "da": da,
        "overtime": overtime_pay,
        "incentives": incentives,
        "gross": gross_salary,
        "deduction": deduction,
        "net": net_salary
    })


# Generate salary statements
print("\n========== EMPLOYEE SALARY STATEMENTS ==========")

for emp in employees:

    print("\n----------------------------------------")
    print("          SALARY STATEMENT")
    print("----------------------------------------")

    print("Employee ID       :", emp["id"])
    print("Employee Name     :", emp["name"])
    print("Basic Pay         : Rs.", round(emp["basic"], 2))
    print("HRA               : Rs.", round(emp["hra"], 2))
    print("DA                : Rs.", round(emp["da"], 2))
    print("Overtime Pay      : Rs.", round(emp["overtime"], 2))
    print("Incentives        : Rs.", round(emp["incentives"], 2))

    print("----------------------------------------")
    print("Gross Salary      : Rs.", round(emp["gross"], 2))
    print("Total Deductions  : Rs.", round(emp["deduction"], 2))
    print("Net Salary        : Rs.", round(emp["net"], 2))
    print("----------------------------------------")
