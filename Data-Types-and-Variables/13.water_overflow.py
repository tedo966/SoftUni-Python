num_lines = int(input())

water_tank_liters = 0

for liters in range(num_lines):
    current_liters = int(input())
    if water_tank_liters + current_liters <= 255:
        water_tank_liters += current_liters
    else:
        print("Insufficient capacity!")

print(water_tank_liters)