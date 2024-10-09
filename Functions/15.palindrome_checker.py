def check_if_palindrome(nums):
    for num in nums:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


my_nums = input().split(', ')
check_if_palindrome(my_nums)


# def check_if_palidnorme(nums):
#     for num in nums:
#         reversed_num = []
#         num.split()
#         for x in num:
#             reversed_num.append(x)
#         reversed_num.reverse()
#         reversed_num = ''.join(reversed_num)
#         if num == reversed_num:
#             print("True")
#         else:
#             print("False")
#
#
# my_nums = input().split(', ')
# check_if_palidnorme(my_nums)