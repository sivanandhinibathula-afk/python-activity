
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
if total_amount >= 10000:
    discount_rate = 20
elif total_amount >= 5000:
    discount_rate = 10
elif total_amount >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = total_amount * discount_rate / 100


max_discount = 1500

if discount > max_discount:
    discount = max_discount


final_bill = total_amount + total_tax - discount


print("\n========== RETAIL INVOICE ==========")
print("Name\tCategory\tPrice\tQty\tSubtotal\tTax")

for p in products:
    print(p[0], "\t", p[1], "\t", p[2],
          "\t", p[3], "\t", p[4], "\t", p[6])

print("------------------------------------")
print("Total Amount :", round(total_amount, 2))
print("Total Tax    :", round(total_tax, 2))
print("Discount Rate:", discount_rate, "%")
print("Discount     :", round(discount, 2))
print("Maximum Limit:", max_discount)
print("------------------------------------")
print("Final Bill   :", round(final_bill, 2))
print("====================================")

