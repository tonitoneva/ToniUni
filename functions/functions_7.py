numbers = input().split(" ")
new_numbers = []
for i in range(len(numbers)):
    new_numbers.append(round(float((numbers[i]))))
print(new_numbers)