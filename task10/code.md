
1. Problem Statement
Develop a Python program for campus event financial planning to calculate the total expenses involved in organizing an event, including venue charges, equipment costs, catering expenses, transportation costs, and certificate costs. The program determines the participant contribution amount, calculates sponsorship shortfalls, and identifies the minimum number of registrations required to break even. Finally, it displays a complete financial report indicating whether the event budget is sufficient.
2. Algorithm
1. Start the program.
2. Enter the event name.
3. Enter venue cost.
4. Enter equipment cost.
5. Enter catering cost per participant.
6. Enter transportation cost.
7. Enter certificate cost per participant.
8. Enter the expected number of participants.
9. Enter the sponsorship amount.
10. Calculate total fixed costs (venue, equipment, and transportation).
11. Calculate variable costs (catering and certificates).
12. Calculate the total event cost.
13. Calculate the sponsorship shortfall, if any.
14. Calculate the amount to be contributed by participants.
15. Calculate the contribution required per participant.
16. Calculate the minimum registration count required to break even.
17. Display the complete financial report.
18. Stop the program.



3. Flowchart – Mermaid Code




<img width="1080" height="1564" alt="image" src="https://github.com/user-attachments/assets/39118a9b-79d6-4dc1-97fa-27a1a5a52b72" />




4. Source Code (Python)





import math

# Campus Event Financial Planning

event = input("Enter event name: ")

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))

sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Calculate fixed costs
fixed_cost = venue + equipment + transport

# Calculate variable cost per participant
variable_cost = catering + certificate

# Calculate total variable cost
total_variable = variable_cost * participants

# Calculate total event cost
total_cost = fixed_cost + total_variable

# Calculate sponsorship shortfall
sponsorship_shortfall = max(0, total_cost - sponsorship)

# Calculate participant contributions
participant_contribution = registration_fee * participants

# Calculate total available income
total_income = sponsorship + participant_contribution

# Calculate surplus or deficit
balance = total_income - total_cost

# Calculate minimum registrations required to break even
remaining_fixed_cost = max(0, fixed_cost - sponsorship)

if remaining_fixed_cost == 0:
    min_registrations = 0
elif registration_fee > variable_cost:
    min_registrations = math.ceil(
        remaining_fixed_cost / (registration_fee - variable_cost)
    )
else:
    min_registrations = "Not possible"

# Display financial report
print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")

print("Event Name:", event)
print("Venue Cost:", venue)
print("Equipment Cost:", equipment)
print("Transport Cost:", transport)
print("Catering Cost:", total_variable -
      certificate * participants)
print("Certificate Cost:", certificate * participants)

print("-----------------------------------------")
print("Fixed Cost:", fixed_cost)
print("Variable Cost:", total_variable)
print("Total Event Cost:", total_cost)

print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", sponsorship_shortfall)

print("Expected Participants:", participants)
print("Registration Fee:", registration_fee)
print("Total Participant Contributions:", participant_contribution)

print("Total Income:", total_income)
print("Surplus / Deficit:", balance)

print("Minimum Break-even Registrations:",
      min_registrations)

if balance >= 0:
    print("Status: Event budget is sufficient")
else:
    print("Status: Event budget is insufficient")

print("=========================================")



5. Source Input



Enter event name: Tech Fest

Enter venue cost: 10000
Enter equipment cost: 5000
Enter transport cost: 3000

Enter catering cost per participant: 200
Enter certificate cost per participant: 50

Enter expected number of participants: 100

Enter sponsorship amount: 15000
Enter registration fee per participant: 300


6. Source Output



===== CAMPUS EVENT FINANCIAL REPORT =====

Event Name: Tech Fest
Venue Cost: 10000.0
Equipment Cost: 5000.0
Transport Cost: 3000.0
Catering Cost: 20000.0
Certificate Cost: 2500.0

-----------------------------------------
Fixed Cost: 18000.0
Variable Cost: 25000.0
Total Event Cost: 43000.0

Sponsorship Amount: 15000.0
Sponsorship Shortfall: 28000.0

Expected Participants: 100
Registration Fee: 300.0
Total Participant Contributions: 30000.0

Total Income: 45000.0
Surplus / Deficit: 2000.0

Minimum Break-even Registrations: 60

Status: Event budget is sufficient
=========================================




