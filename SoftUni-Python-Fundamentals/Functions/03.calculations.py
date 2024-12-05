operation = input()
num_a = int(input())
num_b = int(input())
def calculate(num_a, num_b):
    result = None
    if operation == "multiply":
        result = int(num_a * num_b)
    elif operation == "divide":
        if num_b != 0:
            result = int(num_a / num_b)
        else:
            return "Error: Division by zero"
    elif operation == "add":
        result = int(num_a + num_b)
    elif operation == "subtract":
        result = int(num_a - num_b)
    return result
print(calculate(num_a, num_b))