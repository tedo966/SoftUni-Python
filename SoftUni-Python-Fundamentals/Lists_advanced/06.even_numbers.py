#convert the input in list then with map function convert to int the list
numbers_list = list(map(int,input().split(", ")))


#find the indices of even numbers with map function and lambda function
found_indices = map(
    lambda x: x if numbers_list[x] % 2== 0 else 'no', range(len(numbers_list))
)
# we filter out the even indices and print them
even_indices = list(filter(lambda a: a != "no", found_indices))
print(even_indices)
