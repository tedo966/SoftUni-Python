my_string = input()
my_string = my_string.lower() # convert all letters to lower case
#count if the string contains the word
sand_count = my_string.count("sand")
water_count = my_string.count("water")
fish_count = my_string.count("fish")
sun_count = my_string.count("sun")

total_count = sand_count + water_count + fish_count + sun_count
print(total_count)




