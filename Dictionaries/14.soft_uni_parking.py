num_lines = int(input())
parking_registers = {}

for current_car in range(num_lines):
    command = input().split()
    type_command = command[0]
    name = command[1]
    if type_command == "register":
        car = command[2]
        if name not in parking_registers:
            parking_registers[name] = car
            print(f"{name} registered {car} successfully")
        else:
            print(f"ERROR: already registered with plate number {car}")
    elif type_command == "unregister":
        if name in parking_registers:
            del parking_registers[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")
for name, car in parking_registers.items():
    print(f"{name} => {car}")

