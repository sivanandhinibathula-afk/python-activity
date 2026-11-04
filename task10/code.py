
# Campus Event Financial Planning

# Enter fixed expenses
venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))

# Enter variable expenses per participant
catering_cost = float(input("Enter catering cost per participant: "))
transport_cost = float(input("Enter transport cost per participant: "))
certificate_cost = float(input("Enter certificate cost per participant: "))

# Enter event details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Calculate fixed expenses
fixed_cost = venue_cost + equipment_cost

# Calculate variable cost per participant
variable_cost = catering_cost + transport_cost + certificate_cost

# Calculate total variable expenses
total_variable_cost = variable_cost * participants

# Calculate total event expenses
total_expenses = fixed_cost + total_variable_cost

# Calculate participant contributions
participant_contribution = participants * registration_fee

# Calculate total available funds
total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
sponsorship_shortfall = max(0, total_expenses - participant_contribution - sponsorship)

# Calculate minimum registration count to break even
if registration_fee > variable_cost:
    minimum_registrations = fixed_cost - sponsorship
    minimum_registrations = max(0, minimum_registrations)
    minimum_registrations = int(minimum_registrations // (registration_fee - variable_cost))

    if minimum_registrations * (registration_fee - variable_cost) < fixed_cost - sponsorship:
        minimum_registrations += 1

elif fixed_cost <= sponsorship:
    minimum_registrations = 0

else:
    minimum_registrations = -1


# Display financial report
print("\n========== CAMPUS EVENT FINANCIAL REPORT ==========")

print("Venue Cost: Rs.", round(venue_cost, 2))
print("Equipment Cost: Rs.", round(equipment_cost, 2))
print("Catering Cost Per Participant: Rs.", round(catering_cost, 2))
print("Transport Cost Per Participant: Rs.", round(transport_cost, 2))
print("Certificate Cost Per Participant: Rs.", round(certificate_cost, 2))

print("\nFixed Expenses: Rs.", round(fixed_cost, 2))
print("Variable Cost Per Participant: Rs.", round(variable_cost, 2))
print("Total Variable Expenses: Rs.", round(total_variable_cost, 2))
print("Total Event Expenses: Rs.", round(total_expenses, 2))

print("\nExpected Participants:", participants)
print("Registration Fee Per Participant: Rs.", registration_fee)
print("Participant Contributions: Rs.", round(participant_contribution, 2))
print("Sponsorship Amount: Rs.", round(sponsorship, 2))
print("Total Available Funds: Rs.", round(total_funds, 2))

print("Sponsorship Shortfall: Rs.", round(sponsorship_shortfall, 2))

if minimum_registrations == -1:
    print("Break-even Status: Not possible with current fee and costs")
else:
    print("Minimum Registrations Required:", minimum_registrations)

if total_funds >= total_expenses:
    print("\nEvent Status: Financially Feasible")
    print("Surplus Amount: Rs.", round(total_funds - total_expenses, 2))
else:
    print("\nEvent Status: Additional Funds Required")
    print("Deficit Amount: Rs.", round(total_expenses - total_funds, 2))

print("\n========== END OF REPORT ==========")

