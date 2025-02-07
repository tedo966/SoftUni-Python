# n = int(input())
# matrix = []
# position = []
# stars_collected = 2
# STARS_GOAL = 10
# GAME_OVER = bool
# for r in range(n):
#     matrix.append(input().split())
# for r_i in range(n):
#     if "P" in matrix[r_i]:
#         position = [r_i, matrix[r_i].index("P")]
#         break
#
# directions = {"up": (-1, 0), "down": (1,0), "left":(0, -1), "right":(0, 1)}
#
# while True:
#     direction = input()
#     row = position[0]
#     col = position[1]
#     if matrix[row][col] == "P":
#         matrix[row][col] = "."
#     new_row = row + directions[direction][0]
#     new_col = col + directions[direction][1]
#
#     if stars_collected == STARS_GOAL:
#         GAME_OVER = False
#         break
#     elif stars_collected == 0:
#         GAME_OVER = True
#         break
#
#     if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
#         position = [0, 0]
#         continue
#
#     if matrix[new_row][new_col] == "*":
#         stars_collected += 1
#         matrix[new_row][new_col] = "."
#
#     elif matrix[new_row][new_col] == "#":
#         stars_collected -= 1
#         continue
#
#     position = [new_row, new_col]
#
#
# if GAME_OVER:
#     matrix[row][col] = "P"
#     print(f"Game over! You are out of any stars.\nYour final position is {position}")
#     for el in matrix:
#         print(*el)
# else:
#     matrix[row][col] = "P"
#     print(f"You won! You have collected 10 stars.\nYour final position is {position}")
#     for el in matrix:
#         print(*el)

N = int(input())
stars = 2
start_position = (0, 0)
matrix = []
for row in range(N):
    matrix.append([x for x in input().split()])
    for col in range(N):
        if matrix[row][col] == 'P':
            start_position = (row, col)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    start_row, start_col = start_position
    moves = directions[command]
    new_row, new_col = start_row + moves[0], start_col + moves[1]
    if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
        matrix[start_row][start_col] = '.'
        new_row, new_col = 0, 0
        if matrix[new_row][new_col] == '' and matrix[new_row][new_col] == '.':
            if matrix[new_row][new_col] == '':
                stars += 1
            matrix[new_row][new_col] = 'P'
            start_position = new_row, new_col

        elif matrix[new_row][new_col] == '#':
            stars = 0
            matrix[start_row][start_col] = 'P'
            break

    if matrix[new_row][new_col] == '.':
        matrix[start_row][start_col] = '.'
        matrix[new_row][new_col] = 'P'

    elif matrix[new_row][new_col] == '*':
        stars += 1
        matrix[start_row][start_col] = '.'
        matrix[new_row][new_col] = 'P'
        if stars == 10:
            start_position = new_row, new_col
            break

    elif matrix[new_row][new_col] == '#':
        stars -= 1
        new_row, new_col = start_row, start_col
        if stars == 0:
            break
    start_position = new_row, new_col

if stars == 0:
    print(f'Game over! You are out of any stars.')
    print(f'Your final position is [{", ".join(map(str, start_position))}]')
elif stars >= 10:
    print('You won! You have collected 10 stars.')
    print(f'Your final position is [{", ".join(map(str, start_position))}]')

for m3x in matrix:
    print(' '.join(m3x))