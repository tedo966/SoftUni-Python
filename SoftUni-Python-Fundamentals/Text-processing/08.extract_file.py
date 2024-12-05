my_file = input().split("\\")
subtract_file = my_file[-1].split(".")
filename = subtract_file[0]
extension = subtract_file[1]
print(f"File name: {filename}")
print(f"File extension: {extension}")

