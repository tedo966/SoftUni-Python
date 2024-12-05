
budget = float(input())
price_for_kg_flor =  float(input())

price_eggs_pack = price_for_kg_flor * 0.75 # 1 pack of eggs price
price_liter_milk = price_for_kg_flor * 1.25 # price for 1 liter milk
price_milk_one_loaf = price_liter_milk / 4 # price for 250ml milk
price_for_one_loaf = price_eggs_pack + price_for_kg_flor + price_milk_one_loaf # price for 1 loaf

colored_eggs_received = 0
loaf_counter = 0

while budget >= price_for_one_loaf:
    budget -= price_for_one_loaf
    loaf_counter += 1
    colored_eggs_received += 3
    if loaf_counter % 3 == 0:
        colored_eggs_received -= loaf_counter - 2
print(f"You made {loaf_counter} loaves of Easter bread! Now you have "
      f"{colored_eggs_received} eggs and {budget:.2f}BGN left.")