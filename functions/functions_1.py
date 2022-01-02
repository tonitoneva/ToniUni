numbers = input().split(" ")
new_numbers = []
for i in range(len(numbers)):
    new_numbers.append(abs(float(numbers[i])))
print(new_numbers)


