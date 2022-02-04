n = int(input())
reservations = set()
for _ in range(n):
    code = input()
    reservations.add(code)

guest_code = input()

while not guest_code == "END":
    reservations.remove(guest_code)
    guest_code = input()

print(*{len(reservations)})
print('\n'.join(sorted(reservations)))