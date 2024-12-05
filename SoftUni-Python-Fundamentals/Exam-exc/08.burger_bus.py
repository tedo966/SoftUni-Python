number_of_cities = int(input())
costs = 0
total_profit = 0
for city in range(1, number_of_cities + 1):
    name_city = input()
    owner_income = float(input())
    owner_expense = float(input())

    if city % 3 == 0 and city % 5 == 0:
        owner_income -= owner_income * 0.10
    elif city % 3 == 0:
        owner_expense += owner_expense * 0.5
    elif city % 5 == 0:
        owner_income -= owner_income * 0.10

    profit = owner_income - owner_expense
    print(f"In {name_city} Burger Bus earned {profit:.2f} leva.")
    total_profit += profit

print(f"Burger Bus total profit: {total_profit:.2f} leva.")



