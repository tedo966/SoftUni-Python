list_employees = input().split(" ")
happy_improvement = int(input())
# we multiply each element from list of employees with the happy improvement
list_employees = list(map(lambda x: int(x) * happy_improvement, list_employees))
# we calculate the average of the list of employees
filtered = list(filter(lambda x: x >= (sum(list_employees) / len(list_employees)), list_employees))

if len(filtered) >= len(list_employees) / 2:
    print(f"Score: {len(filtered)}/{len(list_employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(list_employees)}. Employees are not happy!")