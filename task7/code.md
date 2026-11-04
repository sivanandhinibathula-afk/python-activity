# Retail Billing with Multiple Discount Rules – Python Program

## 1. Problem Statement

Develop a Python program to generate a retail bill for multiple products by calculating product prices, quantities, category-specific taxes, threshold-based discounts, and maximum concession limits. The program should calculate the total bill amount and display a detailed billing statement.

## 2. Algorithm

1. Start the program.
2. Initialize an empty product list.
3. Enter the number of products.
4. Enter product name, category, price, and quantity.
5. Calculate the subtotal for each product.
6. Apply category-specific tax rates.
7. Calculate the total amount before discount.
8. Check discount eligibility based on purchase thresholds.
9. Apply the appropriate discount.
10. Check the maximum concession limit.
11. Calculate the final payable amount.
12. Display the detailed retail bill.
13. Stop.

## 3. Flowchart (Mermaid Code)
``` mermaid
flowchart TD
    A([Start]) --> B[Initialize product list]
    B --> C[/Enter number of products/]
    C --> D[/Enter product details/]
    D --> E[Calculate product subtotal]
    E --> F[Calculate category-specific tax]
    F --> G[Calculate total purchase amount]
    G --> H{Check discount threshold}
    H -->|Eligible| I[Calculate discount]
    H -->|Not Eligible| J[Set discount to zero]
    I --> K{Discount exceeds maximum limit?}
    K -->|Yes| L[Apply maximum concession]
    K -->|No| M[Keep calculated discount]
    L --> N[Calculate final bill]
    M --> N
    J --> N
    N --> O[/Display detailed bill/]
    O --> P([Stop])
```

## 5. Sample Input

```
Enter number of products: 3

Enter details of Product 1
Enter product name: Rice
Enter category: food
Enter product price: 1000
Enter quantity: 2

Enter details of Product 2
Enter product name: Shirt
Enter category: clothing
Enter product price: 800
Enter quantity: 2

Enter details of Product 3
Enter product name: Mobile
Enter category: electronics
Enter product price: 10000
Enter quantity: 1
```

## 6. Sample Output

```
========== RETAIL BILL ==========

Product Name: Rice
Category: food
Price: Rs. 1000.0
Quantity: 2
Subtotal: Rs. 2000.0
Tax: Rs. 100.0

Product Name: Shirt
Category: clothing
Price: Rs. 800.0
Quantity: 2
Subtotal: Rs. 1600.0
Tax: Rs. 128.0

Product Name: Mobile
Category: electronics
Price: Rs. 10000.0
Quantity: 1
Subtotal: Rs. 10000.0
Tax: Rs. 1800.0

---------- BILL SUMMARY ----------

Total Subtotal: Rs. 13600.0
Total Tax: Rs. 2028.0
Gross Amount: Rs. 15628.0
Discount Rate: 20 %
Discount Amount: Rs. 1500
Maximum Discount Limit: Rs. 1500
Final Payable Amount: Rs. 14128.0

========== THANK YOU ==========
```

