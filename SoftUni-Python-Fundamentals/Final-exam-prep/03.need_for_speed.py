count_cars = int(input())
my_cars = {}
for current_car in range(count_cars):
    car = input().split("|")
    my_cars[car[0]] = []
    my_cars[car[0]].append(int(car[1]))
    my_cars[car[0]].append(int(car[2]))

command = input()
while command != "Stop":
    tokens = command.split(" : ")
    action = tokens[0]
    car_name = tokens[1]

    if action == "Drive":
        mileage = int(tokens[2])
        fuel = int(tokens[3])
        if car_name in my_cars:
            if fuel > my_cars[car_name][1]:
                print("Not enough fuel to make that ride")
            else:
                my_cars[car_name][0] += mileage
                my_cars[car_name][1] -= fuel
                print(f"{car_name} driven for {mileage} kilometers. {fuel} liters of fuel consumed.")
            if my_cars[car_name][0] >= 100000:
                print(f"Time to sell the {car_name}!")
                my_cars.pop(car_name)
    elif action == "Refuel":
        liters = int(tokens[2])
        liters_in_car = my_cars[car_name][1]
        if liters_in_car + liters > 75:
            refueled_liters = 75 - liters_in_car
            my_cars[car_name][1] += refueled_liters
            print(f"{car_name} refueled with {refueled_liters} liters")
        else:
            print(f"{car_name} refueled with {liters} liters")
            my_cars[car_name][1] += liters

    elif action == "Revert":
        mileages_to_decrease = int(tokens[2])
        my_cars[car_name][0] -= mileages_to_decrease
        if not my_cars[car_name][0] < 10000:
            print(f"{car_name} mileage decreased by {mileages_to_decrease} kilometers")
        else:
            my_cars[car_name][0] = 10000
    command = input()

for car, value in my_cars.items():
    print(f"{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")