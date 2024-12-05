list_of_strings = input().split()

list_of_nums = []

def covert_list_in_nums():
    for num in list_of_strings:
        curr_num = float(num)
        list_of_nums.append(curr_num)
list_of_absolute_nums = []
def choose_absolute_nums():
    for num in list_of_nums:
        absolute_num = abs(num)
        list_of_absolute_nums.append(absolute_num)
    print(list_of_absolute_nums)
covert_list_in_nums()
choose_absolute_nums()