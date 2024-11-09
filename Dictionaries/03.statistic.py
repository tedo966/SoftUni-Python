products = {}

command = input()
while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product not in products:
        products[product] = 0 #we add product with quantity 0
    products[product] += quantity #we change product quantity

    command = input()

print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")


#we print the total products as the length of the products
print(f"Total Products: {len(products.keys())}")
#we print the sum of the values of the products
print(f" Total Quantity: {sum(products.values())}")