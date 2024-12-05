rows = int(input())
while rows > 0:
    number = int(input())
    message = ""
    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number != 88 and number != 86 and number <= 88:
        message = "GREAT!"
    elif number > 88:
        message = "Bye."
    rows -= 1

    print(message)