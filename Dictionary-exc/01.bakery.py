elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    food = elements[i]
    quantity = elements[i + 1]
    bakery[food] = int(quantity)
print(bakery)