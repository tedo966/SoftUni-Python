list_order = {}
line = input()
while line != "buy":
    tokens = line.split()
    price = float(tokens[1])
    quantity = int(tokens[2])
    product = tokens[0]
    if product not in list_order:
        list_order[product] = []
        list_order[product].append(quantity)
        list_order[product].append(price)
    else:
        list_order[product][0] += quantity
        list_order[product][1] = price
    line = input()

for order, price in list_order.items():
    total_price = price[0] * price[1]
    print(f"{order} -> {total_price:.2f}")


