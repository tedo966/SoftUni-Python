nums_list = input().split()

def round_nums():
    rounded_nums = []
    for num in nums_list:
        rounded_num = round(float(num))
        rounded_nums.append(rounded_num)
    return rounded_nums
print(round_nums())