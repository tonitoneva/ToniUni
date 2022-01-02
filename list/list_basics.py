list_of_numbers = input().split()
opposite_numbers = []
for index in range(len(list_of_numbers)):
    opposite_number = -int(list_of_numbers[index])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)


factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)
print(list_of_numbers)