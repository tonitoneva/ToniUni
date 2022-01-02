def even(x):
    return x % 2 == 0

numbers = input().split(" ")
number_as_digit = []
for number in numbers:
    number_as_digit.append(int(number))
result = list(filter(even, (number_as_digit)))
print(result)