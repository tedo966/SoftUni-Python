class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError (Exception):
    pass

class PasswordContainsSpacesError (Exception):
    pass


def password_too_common(pwd, specials):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(c in specials for c in pwd)
    return only_digits or only_letters or only_specials


special_chars = {"@", "*", "&", "%"}


while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError(f"Password must contain at least 8 characters")

    if password_too_common(password, special_chars):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(c in special_chars for c in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if ' ' in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")