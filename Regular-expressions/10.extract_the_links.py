import re
pattern = r'(www\.[-A-Za-z0-9]+(\.[a-z]+)+)'
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        url = match.group(1)
        print(url)
    line = input()