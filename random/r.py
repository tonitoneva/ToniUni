#wateroverflow
number_of_lines = int(input())
capacity = 255
water = 0
for line in range(number_of_lines):
    flow = int(input())
    if capacity - flow < 0:
        print("Insufficient capacity!")
        continue
    water += flow
    capacity -= flow
print (water)

#partyprofit
companions = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    if day % 3 == 0:
        coins -= companions * 3
    if day % 5 == 0:
        coins += companions * 20
        if day % 3 == 0:
            coins -= companions * 2
    coins += 50
    coins -= companions * 2
coins_per_companions = int(coins / companions)
print(f"{companions} companions received {coins_per_companions} coins each.")

