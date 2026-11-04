
products = []

# Enter number of products
n = int(input("Enter number of products: "))

# Enter required profit target
profit_target = float(input("Enter required profit target percentage: "))

for i in range(n):

    print("\nEnter details of Product", i + 1)

    name = input("Enter product name: ")
    quantity = int(input("Enter production quantity: "))

    material_cost = float(input("Enter raw material cost per unit: "))
    labour_cost = float(input("Enter labour charges per unit: "))
    wastage_percent = float(input("Enter material wastage percentage: "))
    machine_cost = float(input("Enter machine cost per unit: "))
    selling_price = float(input("Enter selling price per unit: "))

    # Calculate material wastage
    wastage_cost = material_cost * wastage_percent / 100

    # Calculate total material cost per unit
    total_material = material_cost + wastage_cost

    # Calculate manufacturing cost per unit
    cost_per_unit = total_material + labour_cost + machine_cost

    # Calculate total production cost
    total_cost = cost_per_unit * quantity

    # Calculate total sales revenue
    revenue = selling_price * quantity

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0

    # Check profit target
    if profit_percent >= profit_target:
        status = "Profit Target Achieved"
    else:
        status = "Profit Target Not Achieved"

    # Store product details
    product = {
        "name": name,
        "quantity": quantity,
        "material": material_cost,
        "wastage": wastage_cost,
        "labour": labour_cost,
        "machine": machine_cost,
        "unit_cost": cost_per_unit,
        "total_cost": total_cost,
        "revenue": revenue,
        "profit": profit,
        "profit_percent": profit_percent,
        "status": status
    }

    products.append(product)


# Display manufacturing report
print("\n========== MANUFACTURING REPORT ==========")

for p in products:

    print("\nProduct Name:", p["name"])
    print("Production Quantity:", p["quantity"])
    print("Material Cost Per Unit: Rs.", round(p["material"], 2))
    print("Wastage Cost Per Unit: Rs.", round(p["wastage"], 2))
    print("Labour Cost Per Unit: Rs.", round(p["labour"], 2))
    print("Machine Cost Per Unit: Rs.", round(p["machine"], 2))
    print("Manufacturing Cost Per Unit: Rs.", round(p["unit_cost"], 2))
    print("Total Manufacturing Cost: Rs.", round(p["total_cost"], 2))
    print("Total Sales Revenue: Rs.", round(p["revenue"], 2))
    print("Profit / Loss: Rs.", round(p["profit"], 2))
    print("Profit Percentage:", round(p["profit_percent"], 2), "%")
    print("Production Status:", p["status"])

print("\n========== FINAL SUMMARY ==========")

total_cost = sum(p["total_cost"] for p in products)
total_revenue = sum(p["revenue"] for p in products)
total_profit = total_revenue - total_cost

if total_cost > 0:
    overall_profit = (total_profit / total_cost) * 100
else:
    overall_profit = 0

print("Total Manufacturing Cost: Rs.", round(total_cost, 2))
print("Total Sales Revenue: Rs.", round(total_revenue, 2))
print("Overall Profit / Loss: Rs.", round(total_profit, 2))
print("Overall Profit Percentage:", round(overall_profit, 2), "%")

if overall_profit >= profit_target:
    print("Overall Result: Profit Target Achieved")
else:
    print("Overall Result: Profit Target Not Achieved")

print("\n========== END OF REPORT ==========")

