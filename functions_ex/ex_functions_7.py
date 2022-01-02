numbers = input().split(" ")
number_as_digit = []
for number in numbers:
    number_as_digit.append(int(number))
minimum_number = min(number_as_digit)
maximum_number = max(number_as_digit)
sum_of_numbers = sum(number_as_digit)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_numbers}")