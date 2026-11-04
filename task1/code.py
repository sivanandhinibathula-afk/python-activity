students = []
eligible = []
ineligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    m1 = float(input("Enter Subject 1 marks: "))
    m2 = float(input("Enter Subject 2 marks: "))
    m3 = float(input("Enter Subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total = m1 + m2 + m3
    percentage = total / 3

    if (m1 >= 40 and m2 >= 40 and m3 >= 40
            and percentage >= 60
            and attendance >= 75
            and income <= 250000):

        eligible.append({
            "name": name,
            "percentage": percentage,
            "attendance": attendance,
            "income": income
        })

    else:
        ineligible.append(name)

# Sort based on marks, attendance and income
eligible.sort(
    key=lambda x: (
        -x["percentage"],
        -x["attendance"],
        x["income"]
    )
)

print("\n========== SCHOLARSHIP ELIGIBLE STUDENTS ==========")

if eligible:
    for rank, student in enumerate(eligible, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate Percentage:", round(student["percentage"], 2))
        print("Attendance:", student["attendance"])
        print("Family Income:", student["income"])
        print("Status: Eligible for Scholarship")
else:
    print("No eligible students found.")

print("\n========== INELIGIBLE STUDENTS ==========")

if ineligible:
    for name in ineligible:
        print(name, "- Not Eligible")
else:
    print("All students are eligible.")
