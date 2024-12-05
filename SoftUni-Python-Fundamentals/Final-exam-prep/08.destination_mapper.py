import re
places_map = input()
pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
travel_points = 0

matches = re.findall(pattern, places_map)

my_destinations = [destination for _, destination in matches]
for first_place_length in my_destinations:
    travel_points += len(first_place_length)

my_destinations = ", ".join(my_destinations)
print(f"Destinations: {my_destinations}")
print(f"Travel Points: {travel_points}")

