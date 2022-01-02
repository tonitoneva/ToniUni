def get_even_and_odd_numbers(number):
    sum_even = 0
    sum_odd = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return sum_even, sum_odd

number_as_string = input()
even, odd = get_even_and_odd_numbers(number_as_string)
print(f"Odd sum = {odd}, Even sum = {even}")
