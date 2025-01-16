data = input().split(", ")
rows_count = int(data[0])
cols_count = int(data[1])

matrix = []

max_sum = float("-inf")
sub_matrix = []
for _ in range(rows_count):
    rows_data = [int(el) for el in input().split(", ")]
    matrix.append(rows_data)

for row_index in range(len(matrix)-1):
    for col_index in range(len(matrix[row_index])-1):
        current_el = matrix[row_index][col_index]
        next_to_current = matrix[row_index][col_index+1]
        element_below_curren = matrix[row_index + 1][col_index]
        element_diagonal_current = matrix[row_index+1][col_index+1]

        current_sum = current_el + next_to_current + element_below_curren + element_diagonal_current

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [
                [current_el, next_to_current],
                [element_below_curren, element_diagonal_current]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)