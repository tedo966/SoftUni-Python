number_rooms = int(input())
chairs_left = 0
need_more_chairs_for_room = False
for room in range(1, number_rooms + 1, +1):
    current_room_tokens = input().split()
    if len(current_room_tokens[0]) < int(current_room_tokens[1]):
        need_more_chairs_for_room = True
        needed_chairs = int(current_room_tokens[1]) - len(current_room_tokens[0])
        print(f"{abs(needed_chairs)} more chairs needed in room {room}")
    else:
        current_room_chairs_left = len(current_room_tokens[0]) - int(current_room_tokens[1])
        chairs_left += current_room_chairs_left
if not need_more_chairs_for_room:
    print(f"Game On, {chairs_left} free chairs left")