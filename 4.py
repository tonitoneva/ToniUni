cats = int(input())
group_1 = 0
group_2 = 0
group_3 = 0

sum = 0.0
n = 0

for n in range(cats):
    food = float(input())
    sum += food
    if food >= 100 and food < 200:
        group_1 += 1
    elif food >= 200 and food < 300:
        group_2 += 1
    elif food >= 300 and food <= 400:
        group_3 += 1


total_money_for_day = (sum / 1000) * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day:{total_money_for_day: .2f} lv.")