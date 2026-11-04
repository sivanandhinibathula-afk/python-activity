
# Railway Fare and Reservation Calculator – Python Program

## 1. Problem Statement

Develop a Python program to calculate railway fares for multiple passengers based on travel distance, distance slabs, travel class, age-based concessions, and reservation fees. The program should also calculate cancellation penalties and display the final payable amount for each passenger.

## 2. Algorithm

1. Start the program.
2. Initialize an empty passenger list.
3. Enter the number of passengers.
4. Enter passenger name, age, travel distance, and travel class.
5. Calculate the basic fare based on distance slabs.
6. Apply travel class charges.
7. Check passenger age and apply eligible concessions.
8. Add reservation fees.
9. Calculate the total ticket fare.
10. Ask whether the ticket is cancelled.
11. If cancelled, calculate the cancellation penalty and refund amount.
12. Otherwise, display the payable fare.
13. Repeat for all passengers.
14. Display the final railway fare details.
15. Stop.

## 3. Flowchart (Mermaid Code)
``` mermaid
flowchart TD
    A([Start]) --> B[Initialize passenger list]
    B --> C[/Enter number of passengers/]
    C --> D[/Enter passenger details/]
    D --> E[Calculate distance slab fare]
    E --> F[Apply travel class charges]
    F --> G{Check passenger age}
    G -->|Below 5| H[Free basic fare]
    G -->|5 to 11| I[Apply 50% concession]
    G -->|12 to 59| J[No concession]
    G -->|60 and above| K[Apply 40% concession]
    H --> L[Add reservation fee]
    I --> L
    J --> L
    K --> L
    L --> M[Calculate total fare]
    M --> N{Ticket cancelled?}
    N -->|Yes| O[Calculate cancellation penalty]
    O --> P[Calculate refund amount]
    N -->|No| Q[Calculate payable amount]
    P --> R[Display passenger details]
    Q --> R
    R --> S{More passengers?}
    S -->|Yes| D
    S -->|No| T[/Display final summary/]
    T --> U([Stop])
```



## 5. Sample Input

```
Enter number of passengers: 2

Enter details of Passenger 1
Enter passenger name: Ravi
Enter age: 25
Enter travel distance in KM: 200
Select travel class: 1
Is ticket cancelled? (yes/no): no

Enter details of Passenger 2
Enter passenger name: Sita
Enter age: 65
Enter travel distance in KM: 400
Select travel class: 2
Is ticket cancelled? (yes/no): yes
```

## 6. Sample Output

```
========== RAILWAY FARE REPORT ==========

Passenger Name: Ravi
Age: 25
Distance: 200.0 KM
Travel Class: Sleeper
Base Fare: Rs. 280.0
Age Concession: Rs. 0.0
Reservation Fee: Rs. 40
Total Ticket Fare: Rs. 320.0
Final Payable Amount: Rs. 320.0

Passenger Name: Sita
Age: 65
Distance: 400.0 KM
Travel Class: AC 3 Tier
Base Fare: Rs. 440.0
Age Concession: Rs. 352.0
Reservation Fee: Rs. 40
Total Ticket Fare: Rs. 128.0
Cancellation Penalty: Rs. 32.0
Refund Amount: Rs. 96.0

Total Passengers: 2
========== END OF REPORT ==========
```

