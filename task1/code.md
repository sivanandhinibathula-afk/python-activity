1. Problem Statement




Design and develop a Python program for a University Scholarship Allocation System that evaluates students based on their academic performance, attendance, and family income.

The system should:
1. Accept student details such as name, aggregate marks, subject-wise marks, attendance percentage, and annual family income.
2. Check whether students satisfy the minimum eligibility criteria.
3. Select only eligible students for scholarships.
4. Rank eligible students based on their aggregate marks in descending order.
5. Resolve ties using predefined rules:
   - Higher aggregate marks get higher priority.
   - If aggregate marks are equal, higher attendance gets priority.
   - If both are equal, lower family income gets priority.
6. Display the final scholarship allocation list with student ranks.

  
  
  
  
  2.ALGORITHM

 




1. Start.
2. Read the number of students.
3. For each student, input:
   - Student name
   - Aggregate marks
   - Subject-wise marks
   - Attendance percentage
   - Annual family income
4. Check eligibility conditions:
   - Aggregate marks must be at least 75%.
   - Each subject mark must be at least 50%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
5. If all conditions are satisfied, add the student to the eligible list.
6. Sort eligible students based on:
   - Aggregate marks (descending).
   - Attendance (descending).
   - Annual family income (ascending).
7. Assign ranks to eligible students.
8. Display the eligible students and their ranks.
9. Display rejected students separately.
10. Stop.




3. Flowchart
  
5.  <img width="972" height="1600" alt="image" src="https://github.com/user-attachments/assets/6c0c6f51-4f79-48f2-9ab2-057ea85fa025" />




Flowchart explanation:
- Start the program.
- Enter student information.
- Check eligibility criteria.
- If eligible, add the student to the eligible list.
- Otherwise, reject the student.
- Rank eligible students using the tie-breaking rules.
- Display the scholarship allocation results.
- End the program.


4. Source Code (Python)



  


# Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []
eligible_students = []
rejected_students = []

# Input number of students
n = int(input("Enter number of students: "))

# Collect student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subject_count = int(input("Enter number of subjects: "))
    subject_marks = []

    for j in range(subject_count):
        mark = float(input("Enter subject " + str(j + 1) + " marks: "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = {
        "name": name,
        "aggregate": aggregate,
        "subjects": subject_marks,
        "attendance": attendance,
        "income": income
    }

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARK for mark in subject_marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append(student)

    else:
        rejected_students.append(student)

# Sort eligible students
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"]
    )
)

# Display eligible students
print("\n========== SCHOLARSHIP ALLOCATION ==========")

if eligible_students:
    print("\nEligible Students:")
    print("-" * 75)
    print("Rank\tName\t\tAggregate\tAttendance\tIncome")
    print("-" * 75)

    for rank, student in enumerate(eligible_students, start=1):
        print(
            rank, "\t",
            student["name"], "\t\t",
            student["aggregate"], "\t\t",
            student["attendance"], "\t\t",
            student["income"]
        )
else:
    print("\nNo students are eligible for scholarship.")

# Display rejected students
print("\nRejected Students:")

if rejected_students:
    for student in rejected_students:
        print(student["name"], "- Not eligible")
else:
    print("No rejected students.")

print("\nScholarship allocation completed.")







5. Source Input








========== SCHOLARSHIP ALLOCATION ==========

Eligible Students:
---------------------------------------------------------------------------
Rank    Name       Aggregate   Attendance   Income
---------------------------------------------------------------------------
1       Priya      90.0        95.0         180000.0
2       Anu        90.0        90.0         200000.0
3       Ravi       85.0        95.0         150000.0

Rejected Students:
Kumar - Not eligible

Scholarship allocation completed.



6.SOURCE OUTPUT




========== SCHOLARSHIP ALLOCATION ==========

Eligible Students:
---------------------------------------------------------------------------
Rank    Name       Aggregate   Attendance   Income
---------------------------------------------------------------------------
1       Priya      90.0        95.0         180000.0
2       Anu        90.0        90.0         200000.0
3       Ravi       85.0        95.0         150000.0

Rejected Students:
Kumar - Not eligible

Scholarship allocation completed.

