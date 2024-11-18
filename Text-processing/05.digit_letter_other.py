my_string = input()

spec_symb = ""
letters = ""
numbers = ""
for ch in my_string:
    if ch.isalpha():
        letters += ch
    elif ch.isdigit():
        numbers += ch
    else:
        spec_symb += ch
print(f"{numbers}\n{letters}\n{spec_symb}")