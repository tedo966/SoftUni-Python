n = int(input())
matrix = []
position = [0, 0]


for r in range(n):
    matrix.append(list(input()))
    for c in range(n):
        if matrix[r][c] == "G":
            position = [r, c]
            matrix[r][c] = "-"

amount = 100
directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

command = input()
while command != "end":
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]
    position = [r, c]
    if not (0 <= r < n and 0 <= c < n):
        break
    if matrix[r][c] == "W":
        amount += 100

    elif matrix[r][c] == "P":
        amount -= 200
        if amount <= 0:
            break

    elif matrix[r][c] == "J":
        amount += 100000
        print("You win the Jackpot!")
        break
    command = input()


