# from collections import deque
#
# chocolates = list(map(int, input().split(", ")))
# milk_cups = deque(map(int, input().split(", ")))
# milkshakes = 0
#
# while chocolates and milk_cups:
#     curr_cup = milk_cups[0]
#     curr_chocolate = chocolates[-1]
#
#     if curr_chocolate <= 0:
#         chocolates.pop()
#         continue
#
#     if curr_cup <= 0:
#         milk_cups.popleft()
#         continue
#
#     if curr_chocolate == curr_cup:
#         milkshakes += 1
#         milk_cups.popleft()
#         chocolates.pop()
#     else:
#         milk_cups.rotate(-1)
#         chocolates[-1] -= 5
#
#     if milkshakes == 5:
#         print("Great! You made all the chocolate milkshakes needed!")
#         break
#
# if milkshakes < 5:
#     print("Not enough milkshakes.")
#
# if chocolates:
#     print(f"Chocolate: {', '.join(map(str, chocolates))}")
# else:
#     print("Chocolate: empty")
#
# if milk_cups:
#     print(f"Milk: {', '.join(map(str, milk_cups))}")
# else:
#     print("Milk: empty")

from collections import deque

chocolates = [int(x) for  x in input().split(", ")]
milk_cups = deque(int(x) for  x in input().split(", "))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolates[-1] == milk_cups[0]:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1

    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(x) for x in chocolates]) if  chocolates else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milk_cups]) if  milk_cups else 'empty'}")



