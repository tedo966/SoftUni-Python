n = int(input())
matrix = []
position = [0, 0]
for r in range(n):
    matrix.append(list(input()))
    for c in range(n):
        if matrix[r][c] == "P":
            matrix[r][c] = "-"
            position = [r, c]
health = 100
directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

while True:
    command = input()
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]
    if 0 <= r < n and 0 <= c < n:
        position = [r, c]

        if matrix[r][c] == "X":
            print("Player escaped the maze. Danger passed!")
            break

        elif matrix[r][c] == "H":
            matrix[r][c] = "-"
            health += 15
            if health > 100:
                health = 100

        elif matrix[r][c] == "M":
            health -= 40
            if health > 0:
                matrix[r][c] = "-"
            else:
                health = 0
                print("Player is dead. Maze over!")
                break

print(f"Player's health: {health} units")

matrix[position[0]][position[1]] = "P"
for row in matrix:
    print("".join(row))