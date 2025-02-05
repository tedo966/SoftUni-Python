n = int(input())
matrix = []
resources = 100
for r in range(n):
    curr_col = [x for x in input().split()]
    matrix.append(curr_col)

matrix_position = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for index in range(len(matrix)):
    if 'S' in matrix[index]:
        matrix_position = [int(index), int(matrix[index].index('S'))]
        break
matrix[matrix_position[0]][matrix_position[1]] = "."

direction = input()
while direction:
    move = possible_moves.get(direction)
    if move is None:
        direction = input()
        continue

    row = matrix_position[0] + move[0]
    col = matrix_position[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        print("Mission failed! The spaceship was lost in space.")
        break
    resources -= 5

    matrix_position[0] = row
    matrix_position[1] = col


    if matrix[row][col] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    elif matrix[row][col] == "R":
        resources += 10
        if resources > 100:
            resources = 100

    elif matrix[row][col] == "M":
        resources -= 5
        matrix[row][col] = "."

    if resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

    direction = input()

if not matrix[matrix_position[0]][matrix_position[1]] == "P":
    matrix[matrix_position[0]][matrix_position[1]] = "S"

[print(*row) for row in matrix]



# def initialize_grid_and_start_position(n):
#     grid = []
#     start_pos = None
#     for i in range(n):
#         row = input().split(' ')
#         if 'S' in row:
#             start_pos = (i, row.index('S'))
#         grid.append(row)
#     return grid, start_pos
#
#

# n = int(input())
#
# grid, (x, y) = initialize_grid_and_start_position(n)
# resources = 100
# grid_size = len(grid)
#
# direction_moves = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
#
# # Mark the starting position as '.' when the first move is made
# grid[x][y] = '.'
#
# while True:
#     command = input()
#     dx, dy = direction_moves[command]
#     new_x, new_y = x + dx, y + dy
#
#     if not (0 <= new_x < grid_size) or not (0 <= new_y < grid_size):  # If out of bounds
#         print(f"Mission failed! The spaceship was lost in space.")
#         break
#
#     resources -= 5  # Decrease resources by 5 for moving
#
#     if grid[new_x][new_y] == 'R':
#         resources = min(resources + 10, 100)  # Refuel up to 100
#
#     elif grid[new_x][new_y] == 'M':
#         resources -= 5  # Additional resource loss for meteorite
#         grid[new_x][new_y] = '.'  # Destroy the meteorite
#
#     # Update the spaceship's position
#     x, y = new_x, new_y
#
#     if grid[x][y] == 'P':
#         print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
#         break
#
#     # Check for mission failure only after refueling, to allow refuel at 0 resources
#     if resources < 5:
#         print(f"Mission failed! The spaceship was stranded in space.")
#         break
#
# # Mark the last known position with 'S' if the mission didn't succeed
# if grid[x][y] != 'P':
#     grid[x][y] = 'S'
#
# # Print the final grid state
# for row in grid:
#     print(*row, sep=' ')





