n = int(input())
matrix = []
position = [0, 0]
jetfighter_armor = 300
enemies = 4
for r in range(n):
    matrix.append(list(input()))
    for c in range(n):
        if matrix[r][c] == "J":
            matrix[r][c] = "-"
            position = [r, c]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    r, c = position[0] + moves[command][0], position[1] + moves[command][1]
    position = [r, c]

    if matrix[r][c] == "R":
        matrix[r][c] = "-"
        jetfighter_armor = 300

    elif matrix[r][c] == "E":
        enemies -= 1
        matrix[r][c] = "-"
        if enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        jetfighter_armor -= 100
        if jetfighter_armor <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!")
            break

matrix[position[0]][position[1]] = "J"
for m3x in matrix:
    print("".join(m3x))