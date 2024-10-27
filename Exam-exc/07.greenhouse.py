crops = input().split(" & ")
command = input()
while "Collect!" not in command:
    tokens = command.split()
    to_do = tokens[0]
    crop = tokens[1]
    if to_do == "Plant":
        crops.insert(0,crop)
    elif to_do == "Transplant":
        if crop in crops:
            crops.remove(crop)
            crops.append(crop)
    elif to_do == "Replace":
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        if len(crops) > first_index and len(crops) > second_index:
            swap1,swap2 = first_index,second_index
            crops[swap1], crops[swap2] = crops[swap2], crops[swap1]
    elif to_do == "Uproot":
        if crop in crops:
            crops.remove(crop)

    command = input()
print(f" | ".join(crops))
