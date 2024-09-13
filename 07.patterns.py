large_row_n = int(input())

for i in range (1, large_row_n + 1):
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(large_row_n -1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()
