count_row, count_col = map(int, input().split(", "))
matrix = []
c_position = []
BOMB_TIMER = 16
needed_time = 0
for row in range(count_row):
    matrix.append(list(input()))

is_found_position = False
for i in range(len(matrix)):
    if "C" in matrix[i]:
        is_found_position = True
        c_position = [i, matrix[i].index("C")]
        break

directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
defused = False
while BOMB_TIMER > 0:
    command = input()
    if command != "defuse":
        r = c_position[0] + directions[command][0]
        c = c_position[1] + directions[command][1]
        BOMB_TIMER -= 1

        if 0 <= r < count_row and 0 <= c < count_col:
            c_position = [r, c]
            if matrix[r][c] == "*":
                continue
            elif matrix[r][c] == "B":
                continue
            elif matrix[r][c] == "T":
                matrix[r][c] = "*"
                print("Terrorists win!")
                for row in matrix:
                    print("".join(row))
                exit()
        else:
            continue
    else:
        r, c = c_position[0], c_position[1]
        if matrix[r][c] == "B" and command == "defuse":
            if BOMB_TIMER >= 4:
                BOMB_TIMER -= 4
                matrix[r][c] = "D"
                defused = True
                break
            else:
                needed_time = BOMB_TIMER - 4
                matrix[r][c] = "X"
                break

        elif command == "defuse":
            if BOMB_TIMER >= 2:
                BOMB_TIMER -= 2
                continue
            else:
                needed_time = BOMB_TIMER - 2
                break

if defused:
    print(f"Counter-terrorist wins!\nBomb has been defused: {BOMB_TIMER} second/s remaining.")
    for row in matrix:
        print("".join(row))
else:
    print(f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {abs(needed_time)} second/s.")
    for row in matrix:
        print("".join(row))




