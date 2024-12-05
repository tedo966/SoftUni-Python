command = input().split("#")
amount_water = int(input())
# List to store the water levels
list_fire_out = []
effort = 0
total_fire = 0
for index in range(len(command)):
    # Split in 2 indexes the command
    command_parts = command[index].split(" = ")
    # Convert the water level to integer
    water_out = int(command_parts[1])
    if command_parts[0] == "High" and 81 <= water_out <= 125:
        if water_out <= amount_water:
            amount_water -= water_out
            total_fire += water_out
            effort += water_out * 0.25
            list_fire_out.append(water_out)
    elif command_parts[0] == "Medium" and 51 <= water_out <= 80:
        if water_out <= amount_water:
            amount_water -= water_out
            total_fire += water_out
            effort += water_out * 0.25
            list_fire_out.append(water_out)
    elif command_parts[0] == "Low" and 1 <= water_out <= 50:
        if water_out <= amount_water:
            amount_water -= water_out
            total_fire += water_out
            effort += water_out * 0.25
            list_fire_out.append(water_out)
    else:
        continue

print("Cells:")
for element in list_fire_out:
    print(f" - {element}")
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")

