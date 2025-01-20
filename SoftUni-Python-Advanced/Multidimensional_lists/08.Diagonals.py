# n = int(input())
# #create matrix with the n(rows) and n inputs separated by comma and space
# matrix = [list(map(int, input().split(", "))) for _ in range(n)]
# #iterate trough matrix lists incrementing the element of the current list with 1
# primary_diagonal = [matrix[i][i] for i in range(n)]
# #iterate trough matrix lists from the last element of the current list with  decreasing by 1
# secondary_diagonal = [matrix[i][n-i-1] for i in range(n)]
#
# print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")


n = int(input())
matrix = [[int(x) for x in input().split(", ")]for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1-i] for i in range(n)]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")