import math

def calculate_items_price_for_students(max_price,count_students,flour,eggs, apron):
    free_packs_flour = flour // 5

    total_price_ingredients = apron * (math.ceil(count_students + 0.2)) + eggs * 10 * (count_students) + flour * (count_students - free_packs_flour)
    if total_price_ingredients <= max_price:
        return f"Items purchased for {total_price_ingredients:.2f}$."
    else:
        needed_money = abs(budget - total_price_ingredients)
        return f"{needed_money:.2f}$ more needed."


budget = float(input())
students = int(input())
pack_flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())
result = calculate_items_price_for_students(budget,students,pack_flour_price,single_egg_price,single_apron_price)
print(result)