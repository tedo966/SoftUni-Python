n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n-i-1] for i in range(n)]

difference = sum(primary_diagonal) - sum(secondary_diagonal)

print(abs(difference))