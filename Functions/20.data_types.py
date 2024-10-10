def data_type(type_of_data,command):
    if type_of_data == 'string':
        return f'${command}$'
    if type_of_data == 'real':
        real_num = float(command) * 1.5
        return f"{real_num:.2f}"
    if type_of_data == 'int':
        return int(command) * 2

type_data = input()
command_data = input()
result = data_type(type_data, command_data)
print(result)

# def data_type(type_of_data, command):
#     operations = {
#         'string': lambda x: f'${x}$',
#         'real': lambda x: f"{float(x) * 1.5:.2f}",
#         'int': lambda x: int(x) * 2
#     }
#
#     return operations.get(type_of_data, lambda x: "Invalid type")(command)
#
# type_data = input()
# command_data = input()
# result = data_type(type_data, command_data)
# print(result)

