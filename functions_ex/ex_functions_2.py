def sum_numbers(first_number, second_number):
    return first_number + second_number

def subtract_numbers(two, three):
    return two - three

first = int(input())
second = int(input())
third = int(input())
first_result = sum_numbers(first, second)
second_result = subtract_numbers(first_result, third)
print(second_result)