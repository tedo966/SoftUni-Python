import math
from collections import deque
text_operations = input().split()
nums = deque()
for el in text_operations:
    if el.isdigit() or el.lstrip("-").isdigit():
        nums.append(el)
    else:
        if el == "*":
            while nums:
                if len(nums) <= 1:
                    break
                curr_num = nums.popleft()
                multiply_num = nums.popleft()
                nums.append(int(curr_num) * int(multiply_num))

        elif el == "-":
            while nums:
                if len(nums) <= 1:
                    break
                curr_num = nums.popleft()
                multiply_num = nums.popleft()
                nums.appendleft(int(curr_num) - int(multiply_num))
        elif el == "+":
            while nums:
                if len(nums) <= 1:
                    break
                curr_num = nums.popleft()
                multiply_num = nums.popleft()
                nums.append(int(curr_num) + int(multiply_num))
        elif el == "/":
            while nums:
                if len(nums) <= 1:
                    break
                curr_num = nums.popleft()
                multiply_num = nums.popleft()
                result = int(curr_num) / int(multiply_num)
                nums.appendleft(math.floor(result))
print(*nums)