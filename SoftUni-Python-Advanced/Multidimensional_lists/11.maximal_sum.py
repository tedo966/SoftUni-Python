def read_matrix():
    # Read the dimensions of the matrix
    rows, cols = map(int, input().split())
    matrix = []

    # Read each row of the matrix
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def find_max_3x3(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')  # Initialize maximum sum to a very small number
    best_square = []

    # Iterate through possible starting points of 3x3 submatrices
    for i in range(rows - 2):
        for j in range(cols - 2):
            # Calculate the sum of the current 3x3 submatrix
            current_sum = (
                    matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] +
                    matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] +
                    matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
            )
            # Update max_sum and best_square if the current sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
                best_square = [
                    matrix[i][j:j + 3],
                    matrix[i + 1][j:j + 3],
                    matrix[i + 2][j:j + 3]
                ]

    return max_sum, best_square


def main():
    # Read the matrix from input
    matrix = read_matrix()
    # Find the 3x3 submatrix with the maximum sum
    max_sum, best_square = find_max_3x3(matrix)
    # Print the maximum sum
    print(f"Sum = {max_sum}")
    # Print the best 3x3 submatrix
    for row in best_square:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
