. Problem Statement
Develop a Python program to calculate railway fares for multiple passengers based on distance slabs, travel classes, age-based concessions, and reservation fees. The program should also calculate cancellation penalties and refund amounts when tickets are cancelled, and display the final fare details for all passengers.
2. Algorithm
1. Start the program.
2. Enter the number of passengers.
3. Enter passenger name, age, travel distance, and travel class.
4. Calculate basic fare based on distance:
   - First 100 km – ₹1 per km.
   - Next 200 km – ₹1.5 per km.
   - Above 300 km – ₹2 per km.
5. Calculate fare according to travel class:
   - Sleeper – Basic fare × 1.
   - AC3 – Basic fare × 2.
   - AC2 – Basic fare × 3.
6. Apply age-based concessions:
   - Below 5 years – Free fare.
   - 60 years and above – 40% discount.
   - Others – No discount.
7. Add reservation fee of ₹50.
8. Calculate the final ticket fare.
9. Ask whether the ticket should be cancelled.
10. If cancelled, calculate a 25% cancellation penalty and refund amount.
11. Display passenger ticket details.
12. Repeat for all passengers.
13. Display the total amount.
14. Stop the program.
3. Flowchart (Mermaid Code)


flowchart TD
A([start])-->B[/Enter number of passengers/]
B-->C[/Enter passenger name, age, distance and class/]
C-->D[Calculate basic fare]
D-->E[Calculate class fare]
E-->F{Check age}
F--Below 5-->G[Free fare]
F--60 and above-->H[Apply 40% discount]
F--Others-->I[No discount]
G-->J[Add reservation fee]
H-->J
I-->J
J-->K[Calculate final fare]
K-->L{Cancel ticket?}
L--Yes-->M[Calculate cancellation penalty]
L--No-->N[Confirm ticket]
M-->O[Calculate refund amount]
N-->P[Display passenger details]
O-->P
P-->Q{More passengers?}
Q--Yes-->C
Q--No-->R[Calculate total amount]
R-->S[/Display final bill/]
S-->T([stop])


4. Source Code (Python)

   
# Railway Fare and Reservation Calculator

total_amount = 0

n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("Classes: Sleeper, AC3, AC2")
    travel_class = input("Enter travel class: ").upper()

    # Validate passenger details
    if age < 0 or distance <= 0:
        print("Invalid passenger details!")
        continue

    # Calculate basic fare
    if distance <= 100:
        basic_fare = distance * 1

    elif distance <= 300:
        basic_fare = (100 * 1) + (distance - 100) * 1.5

    else:
        basic_fare = (100 * 1) + (200 * 1.5) + (distance - 300) * 2

    # Calculate class fare
    if travel_class == "SLEEPER":
        class_fare = basic_fare

    elif travel_class == "AC3":
        class_fare = basic_fare * 2

    elif travel_class == "AC2":
        class_fare = basic_fare * 3

    else:
        print("Invalid travel class!")
        continue

    # Apply age concession
    if age < 5:
        discount = class_fare
        reservation_fee = 0

    elif age >= 60:
        discount = class_fare * 0.40
        reservation_fee = 50

    else:
        discount = 0
        reservation_fee = 50

    # Calculate final fare
    fare = class_fare - discount + reservation_fee

    print("\n----- Ticket Details -----")
    print("Passenger Name:", name)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Class Fare: Rs.", round(class_fare, 2))
    print("Concession: Rs.", round(discount, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Final Fare: Rs.", round(fare, 2))

    # Cancellation details
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



5. Sample Input

Enter number of passengers: 2

Passenger 1
Enter passenger name: Ravi
Enter age: 65
Enter travel distance (km): 250
Enter travel class: AC3
Cancel ticket? (yes/no): no

Passenger 2
Enter passenger name: Sita
Enter age: 30
Enter travel distance (km): 150
Enter travel class: SLEEPER
Cancel ticket? (yes/no): yes

6. Sample Output


----- Ticket Details -----

Passenger Name: Ravi
Basic Fare: Rs. 325.0
Class Fare: Rs. 650.0
Concession: Rs. 260.0
Reservation Fee: Rs. 50
Final Fare: Rs. 440.0

Ticket Confirmed.

----- Ticket Details -----

Passenger Name: Sita
Basic Fare: Rs. 175.0
Class Fare: Rs. 175.0
Concession: Rs. 0
Reservation Fee: Rs. 50
Final Fare: Rs. 225.0

Cancellation Penalty: Rs. 56.25
Refund Amount: Rs. 168.75

===== RAILWAY RESERVATION SUMMARY =====

Total Amount: Rs. 496.25

Reservation Process Completed.


