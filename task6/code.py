

total_amount = 0

n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("Classes: Sleeper, AC3, AC2")
    travel_class = input("Enter travel class: ").upper()

    if age < 0 or distance <= 0:
        print("Invalid passenger details!")
        continue

    
    if distance <= 100:
        basic_fare = distance * 1

    elif distance <= 300:
        basic_fare = (100 * 1) + (distance - 100) * 1.5

    else:
        basic_fare = (100 * 1) + (200 * 1.5) + (distance - 300) * 2

    
    if travel_class == "SLEEPER":
        class_fare = basic_fare

    elif travel_class == "AC3":
        class_fare = basic_fare * 2

    elif travel_class == "AC2":
        class_fare = basic_fare * 3

    else:
        print("Invalid travel class!")
        continue

    
    if age < 5:
        discount = class_fare
        reservation_fee = 0

    elif age >= 60:
        discount = class_fare * 0.40
        reservation_fee = 50

    else:
        discount = 0
        reservation_fee = 50

    
    fare = class_fare - discount + reservation_fee

    print("\n----- Ticket Details -----")
    print("Passenger Name:", name)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Class Fare: Rs.", round(class_fare, 2))
    print("Concession: Rs.", round(discount, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Final Fare: Rs.", round(fare, 2))

    
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = fare * 0.25
        refund = fare - penalty

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))

        total_amount += penalty

    else:
        print("Ticket Confirmed.")
        total_amount += fare


print("\n===== RAILWAY RESERVATION SUMMARY =====")
print("Total Amount: Rs.", round(total_amount, 2))
print("Reservation Process Completed.")

