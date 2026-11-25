# Case Study 49: Tuple-Based Product Catalogue Audit

print("PRODUCT CATALOGUE AUDIT")
catalogue = [
    ("P101", 500, 10),
    ("P102", 120, 3),
    ("P103", 0, 8),
    ("P104", 250, -2)
]

inventory_total = 0
reorder_list = []

for product in catalogue:
    product_id, price, stock = product

    if price <= 0 or stock < 0:
        print("Invalid record:", product_id)
    else:
        value = price * stock
        inventory_total += value
        print(product_id, "Inventory Value: Rs.", value)

        if stock < 5:
            reorder_list.append(product_id)

print("Total Valid Inventory Value: Rs.", inventory_total)
print("Products Requiring Replenishment:", reorder_list)
