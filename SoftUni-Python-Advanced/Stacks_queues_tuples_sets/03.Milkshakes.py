from collections import deque

chocolates = list(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))
milkshakes = 0

while chocolates and milk_cups:
    curr_cup = milk_cups[0]
    curr_chocolate = chocolates[-1]

    if curr_chocolate <= 0:
        chocolates.pop()
        continue

    if curr_cup <= 0:
        milk_cups.popleft()
        continue

    if curr_chocolate == curr_cup:
        milkshakes += 1
        milk_cups.popleft()
        chocolates.pop()
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

    if milkshakes == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break

if milkshakes < 5:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(map(str, milk_cups))}")
else:
    print("Milk: empty")


