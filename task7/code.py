
products = []

total_subtotal = 0
total_tax = 0

# Enter number of products
n = int(input("Enter number of products: "))

for i in range(n):

    print("\nEnter details of Product", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ").lower()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Calculate subtotal
    subtotal = price * quantity

    # Category-specific tax
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 8
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 12

    tax = subtotal * tax_rate / 100

    # Store product details
    product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "tax": tax
    }

    products.append(product)

    total_subtotal += subtotal
    total_tax += tax


# Calculate amount before discount
gross_amount = total_subtotal + total_tax

# Threshold-based discount
if gross_amount >= 10000:
    discount_rate = 20
elif gross_amount >= 5000:
    discount_rate = 15
elif gross_amount >= 2000:
    discount_rate = 10
elif gross_amount >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = gross_amount * discount_rate / 100

# Maximum concession limit
max_discount = 1500

if discount > max_discount:
    discount = max_discount

# Calculate final amount
final_amount = gross_amount - discount


# Display bill
print("\n========== RETAIL BILL ==========")

for p in products:

    print("\nProduct Name:", p["name"])
    print("Category:", p["category"])
    print("Price: Rs.", p["price"])
    print("Quantity:", p["quantity"])
    print("Subtotal: Rs.", round(p["subtotal"], 2))
    print("Tax: Rs.", round(p["tax"], 2))

print("\n---------- BILL SUMMARY ----------")

print("Total Subtotal: Rs.", round(total_subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Gross Amount: Rs.", round(gross_amount, 2))
print("Discount Rate:", discount_rate, "%")
print("Discount Amount: Rs.", round(discount, 2))
print("Maximum Discount Limit: Rs.", max_discount)
print("Final Payable Amount: Rs.", round(final_amount, 2))

print("\n========== THANK YOU ==========")

