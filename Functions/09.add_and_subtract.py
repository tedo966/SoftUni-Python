
def sum_numbers(first_num:int, second_num:int) -> int:
    return first_num + second_num

def subtract_nums(result_sum:int, third_num:int) -> int:
    return result_sum - third_num

def add_and_subtract(first_num:int, second_num:int, third_num:int) -> int:
    sum_result = sum_numbers(first_num, second_num)
    final_result = subtract_nums(sum_result, third_num)
    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))