phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name , phone_number = entry.split("-")
    phonebook[name] = phone_number
searches = int(entry)
for current_search in range(searches):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
