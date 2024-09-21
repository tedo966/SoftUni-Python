start_n = int(input())
end_n = int(input())

for index in range(start_n,end_n +1):
    if index == end_n:
        print(chr(index))
    else:
        print(chr(index), end=" ")