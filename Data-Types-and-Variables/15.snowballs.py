number_of_snowballs = int(input())
record_snowball_quality = 0
best_weight = 0
best_speed = 0
best_quality = 0

for snowball_details in range(1,number_of_snowballs + 1):
    weight_of_snowball = int(input())
    speed_of_snowball = int(input())
    quality_snowball = int(input())

    value_of_snowball = (weight_of_snowball / speed_of_snowball) ** quality_snowball
    if value_of_snowball > record_snowball_quality:
        record_snowball_quality = value_of_snowball
        best_weight = weight_of_snowball
        best_speed = speed_of_snowball
        best_quality = quality_snowball
print(f"{best_weight} : {best_speed} = {int(record_snowball_quality)} ({best_quality})")