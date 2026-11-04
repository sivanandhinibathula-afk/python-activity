

passengers = []

# Distance slab fare calculation
def calculate_base_fare(distance):
    if distance <= 100:
        return distance * 1.50
    elif distance <= 300:
        return distance * 1.30
    elif distance <= 500:
        return distance * 1.10
    else:
        return distance * 1.00


# Enter number of passengers
n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nEnter details of Passenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance in KM: "))

    print("Travel Classes:")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")
    print("4. AC First Class")

    choice = int(input("Select travel class: "))

    if choice == 1:
        travel_class = "Sleeper"
        class_charge = 1.0
    elif choice == 2:
        travel_class = "AC 3 Tier"
        class_charge = 2.0
    elif choice == 3:
        travel_class = "AC 2 Tier"
        class_charge = 3.0
    elif choice == 4:
        travel_class = "AC First Class"
        class_charge = 4.0
    else:
        print("Invalid class. Defaulting to Sleeper.")
        travel_class = "Sleeper"
        class_charge = 1.0

    # Calculate basic fare
    base_fare = calculate_base_fare(distance)

    # Apply class charges
    class_fare = base_fare * class_charge

    # Age-based concession
    if age < 5:
        concession = class_fare
    elif age < 12:
        concession = class_fare * 0.50
    elif age >= 60:
        concession = class_fare * 0.40
    else:
        concession = 0

    discounted_fare = class_fare - concession

    # Reservation fee
    reservation_fee = 40

    total_fare = discounted_fare + reservation_fee

    # Cancellation details
    cancel = input("Is ticket cancelled? (yes/no): ").lower()

    if cancel == "yes":
        cancellation_penalty = total_fare * 0.25
        refund = total_fare - cancellation_penalty
        payable = 0
    else:
        cancellation_penalty = 0
        refund = 0
        payable = total_fare

    # Store passenger details
    passenger = {
        "name": name,
        "age": age,
        "distance": distance,
        "class": travel_class,
        "base_fare": base_fare,
        "concession": concession,
        "reservation_fee": reservation_fee,
        "total_fare": total_fare,
        "penalty": cancellation_penalty,
        "refund": refund,
        "payable": payable
    }

    passengers.append(passenger)


# Display final report
print("\n========== RAILWAY FARE REPORT ==========")

for p in passengers:

    print("\nPassenger Name:", p["name"])
    print("Age:", p["age"])
    print("Distance:", p["distance"], "KM")
    print("Travel Class:", p["class"])
    print("Base Fare: Rs.", round(p["base_fare"], 2))
    print("Age Concession: Rs.", round(p["concession"], 2))
    print("Reservation Fee: Rs.", p["reservation_fee"])
    print("Total Ticket Fare: Rs.", round(p["total_fare"], 2))

    if p["penalty"] > 0:
        print("Cancellation Penalty: Rs.",
              round(p["penalty"], 2))
        print("Refund Amount: Rs.",
              round(p["refund"], 2))
    else:
        print("Final Payable Amount: Rs.",
              round(p["payable"], 2))

print("\nTotal Passengers:", len(passengers))
print("========== END OF REPORT ==========")
