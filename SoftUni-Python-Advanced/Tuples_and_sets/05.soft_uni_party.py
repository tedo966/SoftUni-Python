n = int(input())

reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

guest_reservations = input()
while guest_reservations != "END":
    reservations.remove(guest_reservations)
    guest_reservations = input()

print(len(reservations))
for guest in sorted(reservations):
    print(guest)


