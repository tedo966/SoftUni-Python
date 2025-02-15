from collections import deque

amount_money = [int(x) for x in input().split()]
price_foods = deque(int(x) for x in input().split())
food_count = 0
while amount_money and price_foods:
    money = amount_money.pop()
    food_price = price_foods.popleft()

    if money > food_price:
        food_count += 1
        money -= food_price
        if amount_money:
            amount_money[-1] += money
    elif money < food_price:
        continue
    elif money == food_price:
        food_count += 1
        continue
if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count > 1:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")