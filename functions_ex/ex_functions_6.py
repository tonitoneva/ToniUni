numbers = input().split(" ")
number_as_digit = []
for number in numbers:
    number_as_digit.append(int(number))
number_as_digit.sort()
print(number_as_digit)