



MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []
eligible_students = []
rejected_students = []

# Read number of students
n = int(input("Enter number of students: "))

# Get student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subjects = int(input("Enter number of subjects: "))
    subject_marks = []

    for j in range(subjects):
        mark = float(input("Enter subject marks: "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = {
        "name": name,
        "aggregate": aggregate,
        "subject_marks": subject_marks,
        "attendance": attendance,
        "income": income
    }

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subject_marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append(student)
    else:
        rejected_students.append(student)

# Sort eligible students
# Tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income

eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"]
    )
)

# Display scholarship ranking
print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if eligible_students:
    print("\nEligible Students:")
    print("Rank\tName\tAggregate\tAttendance\tIncome")

    for rank, s in enumerate(eligible_students, 1):
        print(
            rank, "\t",
            s["name"], "\t",
            s["aggregate"], "\t\t",
            s["attendance"], "\t\t",
            s["income"]
        )
else:
    print("No eligible students found.")

# Display rejected students
print("\nRejected Students:")

if rejected_students:
    for s in rejected_students:
        print(s["name"], "- Not Eligible")
else:
    print("No rejected students.")

print("\nScholarship allocation completed.")

