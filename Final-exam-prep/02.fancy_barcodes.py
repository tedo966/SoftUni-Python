# import re
# count_codes = int(input())
# pattern = r'@#+([A-Z][A-Za-z0-9]+[A-Z])@#+'
#
# for current_code in range(count_codes):
#
#     barcode = input()
#     match = re.match(pattern, barcode)
#
#     if match and len(match.group(1)) >= 6:
#         product = match.group(1)
#         group = ""
#
#         if any(char.isdigit() for char in product):
#             number = re.findall(r'\d+', product)
#             group += "".join(number)
#         else:
#             group += "00"
#
#         print(f'Product group: {group}')
#     else:
#         print("Invalid barcode")
#
#

import re
number_of_lines = int(input())

pattern = r"@#+[A-Z][A-Z-a-z0-9]{4,}[A-Z]@#+"
product_group = r"\d+"

for lines in range(number_of_lines):
    text = input()
    matches = re.search(pattern, text)

    if matches:
        group = len(re.findall(product_group, matches.group()))
        if group == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(re.findall(product_group, text))}")
    else:
        print("Invalid barcode")


