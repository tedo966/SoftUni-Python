import re
count_messages = int(input())
pattern = r'^([$%])([A-Z][a-z]{2,})\1(:\s()(\[\d+\]\|)(\[\d+\]\|)(\[\d+\]\|)$)'
digit_group = r"\d+"
for _ in range(count_messages):
    message = input()
    valid_message = re.match(pattern, message)
    if valid_message:
        digits = re.findall(digit_group, valid_message.group(3))
        letters = ""
        for current_digit in digits:
            current_digit = int(current_digit)
            letters += chr(current_digit)
        tag = valid_message.group(2)
        print(f"{tag}: {letters}")
    else:
        print("Valid message not found!")


