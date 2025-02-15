def boarding_passengers(capacity, *group_passengers):
    boarded_groups = {}
    total_guests = 0
    all_boarded = False
    list_data = list(group_passengers)

    for count_passengers, program_name in group_passengers:
        if capacity == 0:
            break
        if (capacity - count_passengers) >= 0:
            capacity -= count_passengers
            list_data.remove((count_passengers, program_name))
            if program_name in boarded_groups:
                boarded_groups[program_name] += count_passengers
                continue
            boarded_groups[program_name] = count_passengers
            total_guests += count_passengers


    sorted_groups = sorted(boarded_groups.items(), key=lambda items: (-items[1], items[0]))

    result = ["Boarding details by benefit plan:"]
    for program_name, count_passengers in sorted_groups:
        result.append(f"## {program_name}: {count_passengers} guests")

    if not list_data:
        result.append("All passengers are successfully boarded!")
    else:
        if capacity > 0:
            result.append(f"Partial boarding completed. Available capacity: {capacity}.")
        else:
            result.append("Boarding unsuccessful. Cruise ship at full capacity.")

    return "\n".join(result)

print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
