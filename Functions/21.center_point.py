from math import sqrt
from math import floor


def center_point(x1, y1, x2, y2):
    dist_a = sqrt(x1**2 + y1**2)
    dist_b = sqrt(x2**2 + y2**2)

    if dist_a < dist_b:
        print(f'({floor(x1)}, {floor(y1)})')
    elif dist_a > dist_b:
        print(f'({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x1)}, {floor(y1)})')


user_x1 = float(input())
user_y1 = float(input())
user_x2 = float(input())
user_y2 = float(input())

center_point(user_x1, user_y1, user_x2, user_y2)