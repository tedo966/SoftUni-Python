from xml.etree.ElementInclude import include

n_times = int(input())

while n_times != 0:
    given_str = input()
    if "," in given_str or "." in given_str or "_" in given_str:
        print(f'{given_str} is not pure!')
    else:
        print(f'{given_str} is pure.')
    n_times -= 1