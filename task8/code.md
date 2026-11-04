# Manufacturing Cost and Profitability Analysis – Python Program

## 1. Problem Statement

Develop a Python program to calculate the total manufacturing cost and profitability of products by considering raw material costs, labour charges, material wastage, machine operating costs, and selling prices. The program should calculate the total production cost, profit or loss, profit percentage, and determine whether the production meets the specified profit target.

## 2. Algorithm

1. Start the program.
2. Initialize an empty product list.
3. Enter the number of products to manufacture.
4. Enter product name and production quantity.
5. Enter raw material cost per unit.
6. Enter labour charges per unit.
7. Enter material wastage percentage.
8. Enter machine operating cost per unit.
9. Enter selling price per unit.
10. Enter the required profit target percentage.
11. Calculate material wastage cost.
12. Calculate total material cost.
13. Calculate total labour and machine costs.
14. Calculate total manufacturing cost.
15. Calculate total sales revenue.
16. Calculate profit or loss and profit percentage.
17. Check whether the profit target is achieved.
18. Display the manufacturing cost and profitability report.
19. Stop.

## 3. Flowchart (Mermaid Code)
``` mermaid

flowchart TD
    A([Start]) --> B[Initialize product list]
    B --> C[/Enter number of products/]
    C --> D[/Enter product details/]
    D --> E[Calculate material cost]
    E --> F[Calculate wastage cost]
    F --> G[Calculate labour charges]
    G --> H[Calculate machine cost]
    H --> I[Calculate total manufacturing cost]
    I --> J[Calculate selling revenue]
    J --> K[Calculate profit or loss]
    K --> L[Calculate profit percentage]
    L --> M{Profit meets target?}
    M -->|Yes| N[Production target achieved]
    M -->|No| O[Production target not achieved]
    N --> P[Display manufacturing report]
    O --> P
    P --> Q{More products?}
    Q -->|Yes| D
    Q -->|No| R([Stop])
```

## 5. Sample Input

```
Enter number of products: 2
Enter required profit target percentage: 20

Enter details of Product 1
Enter product name: Chair
Enter production quantity: 100
Enter raw material cost per unit: 500
Enter labour charges per unit: 100
Enter material wastage percentage: 10
Enter machine cost per unit: 50
Enter selling price per unit: 850

Enter details of Product 2
Enter product name: Table
Enter production quantity: 50
Enter raw material cost per unit: 1000
Enter labour charges per unit: 200
Enter material wastage percentage: 5
Enter machine cost per unit: 100
Enter selling price per unit: 1500
```

## 6. Sample Output

```
========== MANUFACTURING REPORT ==========

Product Name: Chair
Production Quantity: 100
Material Cost Per Unit: Rs. 500.0
Wastage Cost Per Unit: Rs. 50.0
Labour Cost Per Unit: Rs. 100.0
Machine Cost Per Unit: Rs. 50.0
Manufacturing Cost Per Unit: Rs. 700.0
Total Manufacturing Cost: Rs. 70000.0
Total Sales Revenue: Rs. 85000.0
Profit / Loss: Rs. 15000.0
Profit Percentage: 21.43 %
Production Status: Profit Target Achieved

Product Name: Table
Production Quantity: 50
Material Cost Per Unit: Rs. 1000.0
Wastage Cost Per Unit: Rs. 50.0
Labour Cost Per Unit: Rs. 200.0
Machine Cost Per Unit: Rs. 100.0
Manufacturing Cost Per Unit: Rs. 1350.0
Total Manufacturing Cost: Rs. 67500.0
Total Sales Revenue: Rs. 75000.0
Profit / Loss: Rs. 7500.0
Profit Percentage: 11.11 %
Production Status: Profit Target Not Achieved

========== FINAL SUMMARY ==========

Total Manufacturing Cost: Rs. 137500.0
Total Sales Revenue: Rs. 160000.0
Overall Profit / Loss: Rs. 22500.0
Overall Profit Percentage: 16.36 %
Overall Result: Profit Target Not Achieved

========== END OF REPORT ==========
```

