numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    #searching for numbers that are equal or less than current_group
    filtered_numbers_for_group = [number for number in numbers if number <= current_group]
    #cleaning the numbers from the filtered
    numbers = [number for number in numbers if number not in filtered_numbers_for_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_group}")
    current_group += 10






