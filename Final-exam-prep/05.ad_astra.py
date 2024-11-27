import re
text_content = input()
pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

matches = re.findall(pattern, text_content)
total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in matches:
    item_name = food[1]
    expiration_date = food[2]
    calories = food[3]

    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")