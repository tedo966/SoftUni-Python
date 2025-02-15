# def move_bee(matrix, direction, bee_position, energy, nectar_collected, restored_energy):
#     n = len(matrix)
#     x, y = bee_position
#
#     if direction == "up":
#         x = (x - 1) % n
#     elif direction == "down":
#         x = (x + 1) % n
#     elif direction == "left":
#         y = (y - 1) % n
#     elif direction == "right":
#         y = (y + 1) % n
#
#     energy -= 1
#
#     if matrix[x][y].isdigit():
#         nectar_collected += int(matrix[x][y])
#         matrix[x][y] = '-'
#
#     if energy <= 0 and not restored_energy and nectar_collected >= 30:
#         restored_energy = True
#         energy += nectar_collected - 30
#         nectar_collected = 30
#
#     return (x, y), energy, nectar_collected, restored_energy
#
#
# # Read input
# n = int(input().strip())
# matrix = []
# bee_position = None
#
# # Fill the matrix and find the bee's initial position
# for i in range(n):
#     row = list(input().strip())
#     if 'B' in row:
#         bee_position = (i, row.index('B'))
#     matrix.append(row)
#
# energy = 15
# nectar_collected = 0
# restored_energy = False
#
# while True:
#     command = input().strip()
#     bee_position, energy, nectar_collected, restored_energy = move_bee(matrix, command, bee_position, energy,
#                                                                        nectar_collected, restored_energy)
#     x, y = bee_position
#
#     if matrix[x][y] == 'H':
#         if nectar_collected >= 30:
#             print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
#         else:
#             print("Beesy did not manage to collect enough nectar.")
#         break
#
#     if energy <= 0:
#         print("This is the end! Beesy ran out of energy.")
#         break
#
# # Update the bee's final position
# final_matrix = [['-' if matrix[i][j] == 'B' else matrix[i][j] for j in range(n)] for i in range(n)]
# final_matrix[bee_position[0]][bee_position[1]] = 'B'
#
# for row in final_matrix:
#     print(''.join(row))

n = int(input())
energy = 15
GOAL_NECTAR = 30
units_nectar = 0
restored_energy = False
matrix = []
position = [0, 0]

for r in range(n):
    matrix.append(list(input()))
    if "B" in matrix[r]:
        position = [r, matrix[r].index("B")]
        matrix[position[0]][position[1]] = "-"

while True:
    command = input()
    nr, nc = position

    if command == "up":
        nr = (nr - 1) % n
    elif command == "down":
        nr = (nr + 1) % n
    elif command == "left":
        nc = (nc - 1) % n
    elif command == "right":
        nc = (nc + 1) % n

    energy -= 1
    if energy <= 0 and not restored_energy and units_nectar >= 30:
        restored_energy = True
        energy += units_nectar - 30
        nectar_collected = 30

    if energy <= 0:
        matrix[nr][nc] = "B"
        print("This is the end! Beesy ran out of energy.")
        break


    if matrix[nr][nc].isdigit():
        units_nectar += int(matrix[nr][nc])
        matrix[nr][nc] = "-"

    if matrix[nr][nc] == "H":
        if units_nectar >= GOAL_NECTAR:
            matrix[nr][nc] = "B"
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            break
        else:
            matrix[nr][nc] = "B"
            print("Beesy did not manage to collect enough nectar.")
            break
    position = [nr, nc]

for row in matrix:
    print("".join(row))