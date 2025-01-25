from functools import reduce

def sum_nums(*args):
    return reduce(lambda x,y: x + y, args)

def subtract_nums(*args):
    return reduce(lambda x, y: x - y, args)

def multiply_nums(*args):
    return reduce(lambda x, y: x * y, args)

def dvide_nums(*args):
    return reduce(lambda x, y: x / y, args) if args[1] != 0 else "Error: Division by zero"


mapper = {"+": sum_nums,
          "-": subtract_nums,
          "*": multiply_nums,
          "/": dvide_nums
          }

def operate(operator, *args):
    return mapper[operator](*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))