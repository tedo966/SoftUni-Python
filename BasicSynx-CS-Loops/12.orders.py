orders = int(input())
total_price = 0
for i in range(0, orders, 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (price_per_capsule > 0 and price_per_capsule <= 100
            and days > 0 and days <= 31
            and capsules_per_day > 0 and capsules_per_day <= 2000):
        price_for_coffee = price_per_capsule * capsules_per_day * days
        total_price += price_for_coffee
    else:
        continue
    print(f'The price for the coffee is: ${price_for_coffee:.2f}')
if total_price != 0:
    print(f'Total: ${total_price:.2f}')


