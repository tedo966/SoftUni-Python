# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':

# Declare a string variable, e.g., sentence = "Learning Python is fun!"
    sentence = "Learning Python is fun!"
# Extract and print a substring, such as the word "Python" from the sentence.
    substring = sentence[9:15]
    print(substring)
# Convert the entire sentence to uppercase and print it.
    sentence_in_upper = sentence.upper()
    print(sentence_in_upper)
# Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
    sentence = sentence.replace("fun","awesome")
    print(sentence)
# If the user chooses Numbers (choice == '2'):
elif choice == '2':
# Prompt the user to input two numbers, e.g., num1 and num2.
    print("Please choose two numbers!")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
# Perform and print the results of addition, subtraction, multiplication, and division.
    add = num1 + num2
    print(f'Now we have added your first number with the second and as result we got \n---> {add}')
    subtraction = num1 - num2
    print(f'Now we have subtracted your first number with the second one and as result we got:\n ---> {subtraction}')
    multiplication = num1 * num2
    print(f'Now we have multiplied your first number with the second one and as result we got:\n ---> {multiplication}')
# Handle division by zero (e.g., print an error message if num2 is zero).
    if num2 == 0:
        print("Error, you can't divide 0 !!!")
    else:
        division = num1 / num2
        print(f'Now we have divided your first number with the second one and as result we got\n ---> {division}')
# Perform a power operation, raising num1 to the power of num2, and print the result.
    raising = num1 **num2
    print(f'Now we have raised your first number with the second one and as result we got\n ---> {raising}')
# If the user chooses Booleans (choice == '3'):
elif choice == '3':
# Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
    is_python_fun = False
    is_sunny = False
# Perform and print the results of logical operations: AND, OR, NOT.
# Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
    python_score = input("How do you score python from 1 to 10? ")
    result_score = int(python_score)
    if result_score > 0 and result_score < 5:
        print("You don't like python at all.")
    if result_score <= 10:
        is_python_fun = True
    else:
        print("You are out of range!")

    weather = input("How many degrees is outside? ")


# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
    pass
# ### List Operations ###
# Create a list with mixed data types (e.g., numbers, strings, booleans).

# Append a new element to the list and print the updated list.

# Access and print the 4th element in the list.

# ### Tuple Operations ###
# Create a tuple with some string elements (e.g., fruits).

# Print the length of the tuple.

# Try to modify one element in the tuple and handle the resulting TypeError.

# ### Dictionary Operations ###
# Create a dictionary with some key-value pairs (e.g., name, age, city).

# Access and print the value for one of the keys (e.g., "age").

# Add a new key-value pair to the dictionary and print the updated dictionary.

# If the user enters an invalid choice:
else:
    pass
# Print an error message indicating an invalid selection.