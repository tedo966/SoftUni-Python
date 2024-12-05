def valid_length(name: str) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False
def containing_requirements(name: str) -> bool:
    for characters in name:
        if not (characters.isalnum() or characters == "-" or characters == "_"):
            return False
    return True
def no_redundant_symbols(name: str) -> bool:
    if " " in name:
        return False
    return True

def all_valid(name: str) -> bool:
    if valid_length(name) and containing_requirements(name) and valid_length(name):
        return True
    return False

usernames = input().split(', ')
for username in usernames:
    if all_valid(username):
        print(username)