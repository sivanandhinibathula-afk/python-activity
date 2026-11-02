1. Problem Statement
Develop a Python program for a retail billing system that processes multiple products and their quantities. The system calculates the total price of each product, applies category-specific taxes, provides discounts based on purchase amount thresholds, and ensures that the total discount does not exceed the maximum concession limit. Finally, it generates an itemized invoice displaying product details, discounts, taxes, and the final payable amount.
2. Algorithm
1. Start the program.
2. Read the number of products.
3. For each product, enter product name, category, price, and quantity.
4. Calculate the subtotal of each product using price × quantity.
5. Calculate tax based on the product category.
6. Add all product subtotals to obtain the total amount.
7. Check the total amount against discount thresholds.
8. Apply the eligible discount percentage.
9. Check whether the discount exceeds the maximum concession limit.
10. If it exceeds the limit, reduce the discount to the maximum limit.
11. Calculate the final bill by adding taxes and subtracting discounts.
12. Display the itemized invoice.
13. Stop the program.
3. Flowchart (Mermaid Code)

<img width="1080" height="1640" alt="image" src="https://github.com/user-attachments/assets/f4c758f6-12a2-4429-a127-210744a33e67" />



4. Source Code (Python)

   
n = int(input("Enter number of products: "))

products = []
total_amount = 0
total_tax = 0

for i in range(n):
    print("\nEnter details of product", i + 1)

    name = input("Product name: ")
    category = input("Category (food/clothing/electronics): ").lower()
    price = float(input("Price per unit: "))
    quantity = int(input("Quantity: "))

    subtotal = price * quantity

    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 8
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 10

    tax = subtotal * tax_rate / 100
    total = subtotal + tax

    total_amount += subtotal
    total_tax += tax

    products.append([name, category, price, quantity,
                     subtotal, tax_rate, tax, total])

# Discount calculation
if total_amount >= 10000:
    discount_rate = 20
elif total_amount >= 5000:
    discount_rate = 10
elif total_amount >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = total_amount * discount_rate / 100

# Maximum concession limit
max_discount = 1500

if discount > max_discount:
    discount = max_discount

# Final bill calculation
final_bill = total_amount + total_tax - discount

# Display invoice
print("\n========== RETAIL INVOICE ==========")

print("\nName       Category    Price  Qty  Subtotal  Tax")

for p in products:
    print(p[0], p[1], p[2], p[3], p[4],
          p[6])

print("------------------------------------")
print("Total Amount  :", total_amount)
print("Total Tax     :", total_tax)
print("Discount Rate :", discount_rate, "%")
print("Discount      :", discount)
print("Maximum Limit :", max_discount)
print("------------------------------------")
print("Final Bill    :", final_bill)
print("====================================")



5. Source Input
Example input:

Enter number of products: 3

Enter details of product 1
Product name: Rice
Category: food
Price per unit: 100
Quantity: 10

Enter details of product 2
Product name: Shirt
Category: clothing
Price per unit: 500
Quantity: 5

Enter details of product 3
Product name: Laptop
Category: electronics
Price per unit: 20000
Quantity: 1


6. Source Output


   ========== RETAIL INVOICE ==========

Name       Category    Price  Qty  Subtotal  Tax

Rice       food        100    10   1000      50
Shirt      clothing    500    5    2500      200
Laptop     electronics 20000  1    20000     3600

------------------------------------
Total Amount  : 23500
Total Tax     : 3850
Discount Rate : 20 %
Discount      : 1500
Maximum Limit : 1500
------------------------------------
Final Bill    : 25850
====================================


