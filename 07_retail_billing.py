# Case Study 7: Retail Billing with Multiple Discount Rules

print("RETAIL BILL")
names = ["Rice Bag", "Notebook", "Water Bottle"]
prices = [1200, 80, 250]
quantities = [1, 5, 2]
categories = ["Food", "Other", "Other"]

subtotal = 0
total_tax = 0

for i in range(len(names)):
    amount = prices[i] * quantities[i]
    if categories[i] == "Food":
        tax = amount * 0.05
    else:
        tax = amount * 0.12
    subtotal = subtotal + amount
    total_tax = total_tax + tax
    print(names[i], "Qty:", quantities[i], "Amount:", amount, "Tax:", tax)

if subtotal >= 2000:
    discount = subtotal * 0.10
else:
    discount = 0

if discount > 500:
    discount = 500

final_bill = subtotal + total_tax - discount
print("Subtotal: Rs.", subtotal)
print("Total Tax: Rs.", total_tax)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_bill)
