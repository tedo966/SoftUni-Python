#matrix dimensions
rows, cols = map(int, input().split())

#create the matrix
matrix = [input().split() for _ in range(rows)]

count_identical = 0

for i in range(rows -1):
    for j in range(cols -1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            count_identical += 1
print(count_identical)