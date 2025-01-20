r, c = map(int, input().split())

matrix = []
for i in range(r):
    curr_letter = chr(97 + i)
    matrix.append([])
    for j in range(c):
        next_letter = ord(curr_letter) + j
        matrix[i].append(curr_letter + chr(next_letter) + curr_letter)
for el in range(len(matrix)):
    print(' '.join(matrix[el]))


