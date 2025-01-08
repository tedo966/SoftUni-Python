from collections import deque
name = input()
customers = deque()

while name != "End":
    # check if name is == Paid remove from customers the names of people who has paid
    if name == "Paid":
        while customers:
            print(customers.popleft())
    # append the name to customers until command end or paid
    else:
        customers.append(name)

    name = input()
# print the remaining customers who have not paid
print(f"{len(customers)} people remaining.")