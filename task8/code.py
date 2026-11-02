


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
              wastage_cost + machine_cost
cost_per_unit = total_cost / quantity


selling_price = float(input("Enter selling price per unit: "))


total_revenue = selling_price * quantity
profit = total_revenue - total_cost
profit_target = float(input("Enter profit target: "))


print("\n===== MANUFACTURING REPORT =====")
print("Product Name        :", product)
print("Quantity Produced   :", quantity)
print("Material Cost       :", total_material)
print("Labour Cost         :", total_labour)
print("Wastage Cost        :", wastage_cost)
print("Machine Cost        :", machine_cost)
print("Total Manufacturing:", total_cost)
print("Cost Per Unit       :", cost_per_unit)
print("Selling Price       :", selling_price)
print("Total Revenue       :", total_revenue)
print("Total Profit        :", profit)
print("Profit Target       :", profit_target)

if profit >= profit_target:
    print("Result: Production meets the profit target.")
else:
    print("Result: Production does not meet the profit target.")

print("================================")

