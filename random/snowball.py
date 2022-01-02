from math import pow
number_of_snowballs = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0
for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_snowball_value = int(pow(weight / time, quality))
    if current_snowball_value > max_value:
        max_value = current_snowball_value
        max_weight = weight
        max_time = time
        max_quality = quality
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")