items = input().split("|")
budget = int(input())

max_clothes_price = 50
max_shoes_price = 35
max_accessories_price = 20.50
ticket_price_france = 150
profit = 0
list_prices_profit = []

for type_product in range(len(items)):
    product_info = items[type_product].split("->")
    product_name = product_info[0]
    product_price = float(product_info[1])
    if budget >= product_price:

        if product_name == "Clothes" and max_clothes_price >= product_price:
            budget -= product_price
            profit += product_price * 0.4
            list_prices_profit.append(product_price * 0.4 + product_price)
        elif product_name == "Shoes" and max_shoes_price >= product_price:
            budget -= product_price
            profit += product_price * 0.4
            list_prices_profit.append(product_price * 0.4 + product_price)
        elif product_name == "Accessories" and max_accessories_price >= product_price:
            budget -= product_price
            profit += product_price * 0.4
            list_prices_profit.append(product_price * 0.4 + product_price)
        else:
            continue
# Print the prices with the profit to second decimal point from the list_prices_profit
print(' '.join([f"{price:.2f}" for price in list_prices_profit]))
print(f"Profit: {profit:.2f}")
for element in list_prices_profit:
    budget += element

if budget >= ticket_price_france:
    print("Hello, France!")
else:
    print("Not enough money.")
