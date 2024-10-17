def electron_distribution(electrons):
    shells = []
    n = 1

    while electrons > 0:
        max_electrons = 2 * (n ** 2)
        if electrons >= max_electrons:
            shells.append(max_electrons)
        else:
            shells.append(electrons)

        electrons -= max_electrons
        n += 1

    return shells


electrons = int(input())
result = electron_distribution(electrons)
print(result)
