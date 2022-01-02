locations = int(input())

total_per_location = 0

for i in range(0, locations):
    expected_average_per_day = float(input())
    days_to_dig = int(input())
    for j in range(0, days_to_dig):
        actual_per_day = float(input())
        total_per_location += actual_per_day
    if (total_per_location / days_to_dig) >= expected_average_per_day:
        print(f"Good job! Average gold per day:{(total_per_location / days_to_dig): .2f}.")
    else:
        print(f"You need{(expected_average_per_day - (total_per_location / days_to_dig)): .2f} gold.")
    total_per_location = 0