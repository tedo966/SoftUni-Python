def calculate_plunder_earned(days,plunder,range):
    total_plunder = 0
    day = 1
    while days:
        total_plunder += plunder
        if day % 3 == 0:
            add_additional_plunder = plunder * 0.5
            total_plunder += add_additional_plunder
        if day % 5 == 0:
            total_plunder -= (total_plunder * 0.3)

        day += 1
        days -= 1
    if range <= total_plunder:
        return f"Ahoy! {total_plunder:.2f} plunder gained."
    else:
        collected_percentage = (total_plunder / range) * 100
        return f"Collected only {collected_percentage:.2f}% of the plunder."
days_of_plunder = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
result = calculate_plunder_earned(days_of_plunder, plunder_per_day, expected_plunder)
print(result)