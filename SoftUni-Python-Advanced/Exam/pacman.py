n = int(input())
matrix = []
position = [0, 0]
health = 100
stars = 0
freeze_shield = 0
victory = False
game_over = False

for r in range(n):
    matrix.append(list(input()))
    for c in range(n):
        if matrix[r][c] == "P":
            matrix[r][c] = "-"
            position = [r, c]
        elif matrix[r][c] == "*":
            stars += 1

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
command = input()

while command != "end":
    r, c = position[0] + moves[command][0], position[1] + moves[command][1]
    if not (0 <= r < n and 0 <= c < n):
        r = r % n
        c = c % n
    position = [r, c]

    if matrix[r][c] == "F":
        freeze_shield += 1
        matrix[r][c] = "-"
    elif matrix[r][c] == "*":
        stars -= 1
        matrix[r][c] = "-"
        if stars == 0:
            victory = True
            break
    elif matrix[r][c] == "G":
        if freeze_shield > 0:
            freeze_shield -= 1
        else:
            health -= 50
        matrix[r][c] = "-"
        if health <= 0:
            game_over = True
            break

    command = input()

if victory:
    print("Pacman wins! All the stars are collected.")
    print(f"Health: {health}")

if game_over:
    print(f"Game over! Pacman last coordinates [{position[0]},{position[1]}]")
    print(f"Health: {health}")
    if stars > 0:
        print(f"Uncollected stars: {stars}")

if not game_over and not victory:
    print("Pacman failed to collect all the stars.")
    print(f"Health: {health}")
    if stars > 0:
        print(f"Uncollected stars: {stars}")

matrix[position[0]][position[1]] = "P"
for row in matrix:
    print("".join(row))




