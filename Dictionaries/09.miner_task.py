command = input()
my_resources = {}
while command != "stop":
    quantity = int(input())
    if command in my_resources:
        my_resources[command] += quantity
    else:
        my_resources[command] = quantity
    command = input()
for resource in my_resources:
    print(f"{resource} -> {my_resources[resource]}")
