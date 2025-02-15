from collections import deque

total_count_pie_contestant_consume = deque(map(int, input().split()))
pies = list(map(int, input().split()))

while total_count_pie_contestant_consume and pies:
    current_contestant_capacity, current_pie = total_count_pie_contestant_consume.popleft(), pies.pop()

    if current_contestant_capacity >= current_pie:
        current_contestant_capacity -= current_pie

        if current_contestant_capacity > 0:
            total_count_pie_contestant_consume.append(current_contestant_capacity)

    elif current_pie > current_contestant_capacity:
        current_pie -= current_contestant_capacity
        if pies and current_pie == 1:
            pies[-1] += current_pie
        else:
            pies.append(current_pie)


if not total_count_pie_contestant_consume and not pies:
    print("We have a champion!")
elif pies:
    print("Our contestants need to rest!")
    print(f'Pies left: {", ".join(str(pies) for pies in pies)}')
elif total_count_pie_contestant_consume:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(total_count_pie_contestant_consume) for total_count_pie_contestant_consume in total_count_pie_contestant_consume)}")