def check_length(my_pass): #It should be 6 - 10 (inclusive) characters long
    if 6 <= len(my_pass) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return False
def check_digit_letters(my_pass): #It should consist only of letters and digits
    if my_pass.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False
def check_count_digits(my_pass): #It should have at least 2 digits
    count_digits = 0
    for i in range(len(my_pass)):
        if my_pass[i].isdigit():
            count_digits += 1
    if count_digits < 2:
        print("Password must have at least 2 digits")
        return False
    else:
        return True
def is_valid_password(my_pass): # If a password is valid, print "Password is valid".
    valid_length = check_length(my_pass)
    valid_chars = check_digit_letters(my_pass)
    valid_digits = check_count_digits(my_pass)
    if valid_length and valid_chars and valid_digits:
        print("Password is valid")

inputed_password = input()
is_valid_password(inputed_password)