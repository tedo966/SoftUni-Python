elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    food = elements[i]
    quantity = elements[i + 1]
    bakery[food] = int(quantity)

search_for_products = input().split()

for product in search_for_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")