current_command = input().split()
user_sides = {}

while True:
    if "|" in current_command:

        force_side = current_command[0]
        force_user = current_command[2]


        if force_side and force_user not in user_sides:
            user_sides[force_side] = []
            user_sides[force_side].append(force_user)



    elif "->" in current_command:
        pass

    current_command = input().split()