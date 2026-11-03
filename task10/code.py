
import math



event = input("Enter event name: ")


venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))

sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))


fixed_cost = venue + equipment + transport


variable_cost = catering + certificate
total_variable = variable_cost * participants


total_cost = fixed_cost + total_variable


sponsorship_shortfall = max(0, total_cost - sponsorship)


participant_contribution = registration_fee * participants


total_income = sponsorship + participant_contribution


balance = total_income - total_cost


remaining_fixed_cost = max(0, fixed_cost - sponsorship)

if remaining_fixed_cost == 0:
    min_registrations = 0
elif registration_fee > variable_cost:
    min_registrations = math.ceil(
        remaining_fixed_cost / (registration_fee - variable_cost)
    )
else:
    min_registrations = "Not possible"


print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")

print("Event Name:", event)
print("Venue Cost:", venue)
print("Equipment Cost:", equipment)
print("Transport Cost:", transport)
print("Catering Cost:", catering * participants)
print("Certificate Cost:", certificate * participants)

print("-----------------------------------------")
print("Fixed Cost:", fixed_cost)
print("Variable Cost:", total_variable)
print("Total Event Cost:", total_cost)

print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", sponsorship_shortfall)

print("Expected Participants:", participants)
print("Registration Fee:", registration_fee)
print("Participant Contributions:", participant_contribution)

print("Total Income:", total_income)
print("Surplus / Deficit:", balance)

print("Minimum Break-even Registrations:", min_registrations)

if balance >= 0:
    print("Status: Event budget is sufficient")
else:
    print("Status: Event budget is insufficient")

print("=========================================")

