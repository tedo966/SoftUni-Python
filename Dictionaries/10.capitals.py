country = input().split(", ")
capitals = input().split(", ")
my_dict = {k:v for (k,v) in zip(country,capitals)}
for country in my_dict:
    print(f"{country} -> {my_dict[country]}")

#
# for i in range(len(country)):
#     my_dictionary[country[i]] = capitals[i]




