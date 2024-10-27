days_vacation = int(input())
budget = int(input())
count_people = int(input())
price_fuel_per_km = float(input())
food_expenses_per_person = float(input())
night_price_per_person = float(input())

accommodation_price = count_people * night_price_per_person * days_vacation

if count_people > 10:
    accommodation_price = accommodation_price * 0.75
total_price_expenses= (food_expenses_per_person * count_people * days_vacation) + accommodation_price


for day in range(1, days_vacation + 1):
    traveled_km = float(input())
    total_price_expenses += traveled_km * price_fuel_per_km

    if day % 3 == 0 or day % 5 == 0:
        additional_expenses = (total_price_expenses * 0.4)
        total_price_expenses += additional_expenses

    elif day % 7 == 0:
        extra_money_added = total_price_expenses / count_people
        total_price_expenses -= extra_money_added

    if total_price_expenses > budget:
        print(f"Not enough money to continue the trip. You need {abs(total_price_expenses - budget):.2f}$ more.")
        exit()


print(f"You have reached the destination. You have {budget - total_price_expenses:.2f}$ budget left.")
