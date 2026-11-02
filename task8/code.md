1. Problem Statement
Develop a Python program to calculate the total manufacturing cost and profitability of a product by considering material costs, labour charges, wastage costs, and machine operating costs. Calculate the total production cost, cost per unit, selling price, total revenue, and profit. Finally, compare the profit with a specified profit target and identify whether the production meets the target.
2. Algorithm
1. Start the program.
2. Enter the product name.
3. Enter the number of units produced.
4. Enter the material cost per unit.
5. Enter the labour charges per unit.
6. Enter the wastage percentage.
7. Enter the machine operating cost.
8. Calculate the total material cost.
9. Calculate the total labour cost.
10. Calculate the wastage cost.
11. Calculate the total manufacturing cost.
12. Calculate the manufacturing cost per unit.
13. Enter the selling price per unit.
14. Calculate the total revenue.
15. Calculate the total profit.
16. Enter the required profit target.
17. Compare actual profit with the target.
18. Display all manufacturing costs and profitability details.
19. Stop the program.
3. Flowchart – Mermaid Code



<img width="1080" height="1564" alt="image" src="https://github.com/user-attachments/assets/c21152b4-8c00-4880-867e-0563003d335f" />


4. Source Code (Python)





product = input("Enter product name: ")
quantity = int(input("Enter number of units produced: "))

material_cost = float(input("Enter material cost per unit: "))
labour_cost = float(input("Enter labour charges per unit: "))
wastage_percent = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter total machine cost: "))


total_material = material_cost * quantity
total_labour = labour_cost * quantity


wastage_cost = total_material * wastage_percent / 100


total_cost = (total_material + total_labour +
              wastage_cost + machine_cost)

cost_per_unit = total_cost / quantity


selling_price = float(input("Enter selling price per unit: "))
total_revenue = selling_price * quantity


profit = total_revenue - total_cost


profit_target = float(input("Enter profit target: "))


print("\n===== MANUFACTURING REPORT =====")
print("Product Name       :", product)
print("Quantity Produced  :", quantity)
print("Material Cost      :", total_material)
print("Labour Cost        :", total_labour)
print("Wastage Cost       :", wastage_cost)
print("Machine Cost       :", machine_cost)
print("Total Manufacturing:", total_cost)
print("Cost Per Unit      :", cost_per_unit)
print("Selling Price      :", selling_price)
print("Total Revenue      :", total_revenue)
print("Total Profit       :", profit)
print("Profit Target      :", profit_target)


if profit >= profit_target:
    print("Result: Production meets the profit target.")
else:
    print("Result: Production does not meet the profit target.")

print("===============================")





5. Source Input


Enter product name: Chair
Enter number of units produced: 100
Enter material cost per unit: 200
Enter labour charges per unit: 50
Enter wastage percentage: 10
Enter total machine cost: 2000
Enter selling price per unit: 350
Enter profit target: 5000


6. Source Output



===== MANUFACTURING REPORT =====
Product Name       : Chair
Quantity Produced  : 100
Material Cost      : 20000
Labour Cost        : 5000
Wastage Cost       : 2000
Machine Cost       : 2000
Total Manufacturing: 29000
Cost Per Unit      : 290
Selling Price      : 350
Total Revenue      : 35000
Total Profit       : 6000
Profit Target      : 5000

Result: Production meets the profit target.
===============================




