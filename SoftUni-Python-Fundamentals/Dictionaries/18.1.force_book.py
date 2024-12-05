def add_or_del_user(side_dict, force_user, force_side):
    for key, value in side_dict.items():
        if force_user in value:
            side_dict[key].remove(force_user)
            break
    if force_side not in side_dict:
        side_dict[force_side] = []
    side_dict[force_side].append(force_user)
    return side_dict


def add_new_user(side_dict, force_user, force_side):
    if not any(force_user in users for users in side_dict.values()):
        if force_side not in side_dict:
            side_dict[force_side] = []
        side_dict[force_side].append(force_user)
    return side_dict


side = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if "|" in line:
        force_side, force_user = line.split(" | ")
        side = add_new_user(side, force_user, force_side)

    elif "->" in line:
        force_user, force_side = line.split(" -> ")
        side = add_or_del_user(side, force_user, force_side)
        print(f"{force_user} joins the {force_side} side!")

for force_side, users in side.items():
    if users:
        print(f"Side: {force_side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")