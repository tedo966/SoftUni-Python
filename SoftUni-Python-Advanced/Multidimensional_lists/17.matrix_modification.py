n = int(input())
matrix = []
for r in range(n):
    curr_col = [int(x) for x in input().split()]
    matrix.append(curr_col)


command = input().split()
while command[0] != "END":

    row, col, given_num = int(command[1]), int(command[2]), int(command[3])

    if row and col > (n-1) or row and col < 0:
        print("Invalid coordinates")
        command = input().split()
        continue

    if command[0] == "Add":
        matrix[row][col] += given_num

    elif command[0] == "Subtract":
        matrix[row][col] -= given_num

    command = input().split()


