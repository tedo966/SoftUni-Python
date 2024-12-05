order = input()
count_drinks = int(input())
coffee = 1.50
water = 1
coke = 1.40
snacks = 2
def sum_price(count: int):
    total_price = 0
    if order == "coffee":
        total_price = coffee * count
    elif order == "water":
        total_price = water * count
    elif order == "coke":
        total_price = coke * count
    elif order == "snacks":
        total_price = snacks * count
    return f'{total_price:.2f}'

print(sum_price(count_drinks))