names_list = input().split(", ")
# with sort sorts the list alphabetically
names_list.sort()
# we sort the list by the length
sort_by_length = sorted(names_list, key=lambda x: (-len(x), x))
print(sort_by_length)