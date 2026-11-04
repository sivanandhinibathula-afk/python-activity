# University Scholarship Allocation System Using Python

## 1. Problem Statement

Design and develop a Python program for a University Scholarship Allocation System. The system evaluates students based on aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income. Students who satisfy all the eligibility criteria are considered eligible for scholarships. The system ranks eligible students based on aggregate marks in descending order. If two or more students have equal aggregate marks, ties are resolved using higher attendance percentage, followed by lower family income. Finally, the program displays the list of eligible students along with their ranks and scholarship eligibility status.

## 2. Algorithm

1. Start the program.
2. Read the number of students.
3. For each student, input:
   - Student name
   - Marks in three subjects
   - Attendance percentage
   - Annual family income
4. Calculate the aggregate marks.
5. Check whether each subject mark is at least 40.
6. Check whether aggregate percentage is at least 60%.
7. Check whether attendance is at least 75%.
8. Check whether annual family income is less than or equal to ₹2,50,000.
9. If all conditions are satisfied, declare the student eligible.
10. Store all eligible students in a list.
11. Sort eligible students based on:
    - Higher aggregate percentage.
    - Higher attendance percentage.
    - Lower family income.
12. Assign ranks to eligible students.
13. Display eligible students with their ranks.
14. Display ineligible students separately.
15. Stop the program.

## 3. Flowchart 
``` mermaid
flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student name, subject marks, attendance and income/]
    C --> D[Calculate aggregate marks and percentage]
    D --> E{All subject marks >= 40?}
    E -- No --> K[Declare student ineligible]
    E -- Yes --> F{Aggregate percentage >= 60?}
    F -- No --> K
    F -- Yes --> G{Attendance >= 75?}
    G -- No --> K
    G -- Yes --> H{Family income <= 250000?}
    H -- No --> K
    H -- Yes --> I[Add student to eligible list]
    I --> L{More students?}
    K --> L
    L -- Yes --> C
    L -- No --> M[Sort eligible students by marks, attendance and income]
    M --> N[Assign ranks]
    N --> O[/Display eligible students and ranks/]
    O --> P[/Display ineligible students/]
    P --> Q([Stop])
```
## 5. Sample Input

```
Enter number of students: 4

Enter details of Student 1
Enter student name: Ravi
Enter Subject 1 marks: 85
Enter Subject 2 marks: 90
Enter Subject 3 marks: 80
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Priya
Enter Subject 1 marks: 90
Enter Subject 2 marks: 85
Enter Subject 3 marks: 95
Enter attendance percentage: 95
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Kumar
Enter Subject 1 marks: 70
Enter Subject 2 marks: 75
Enter Subject 3 marks: 80
Enter attendance percentage: 80
Enter annual family income: 220000

Enter details of Student 4
Enter student name: Anu
Enter Subject 1 marks: 35
Enter Subject 2 marks: 80
Enter Subject 3 marks: 75
Enter attendance percentage: 85
Enter annual family income: 150000
```

## 6. Sample Output

```
========== SCHOLARSHIP ELIGIBLE STUDENTS ==========

Rank: 1
Name: Priya
Aggregate Percentage: 90.0
Attendance: 95.0
Family Income: 180000.0
Status: Eligible for Scholarship

Rank: 2
Name: Ravi
Aggregate Percentage: 85.0
Attendance: 90.0
Family Income: 200000.0
Status: Eligible for Scholarship

Rank: 3
Name: Kumar
Aggregate Percentage: 75.0
Attendance: 80.0
Family Income: 220000.0
Status: Eligible for Scholarship

========== INELIGIBLE STUDENTS ==========

Anu - Not Eligible
```
