number = int(input())
key = input()
list_of_strings = []
for word in range (number):
    string = input()
    list_of_strings.append(string)
print(list_of_strings)
for i in range(len(list_of_strings) -1, -1, -1):
    element = list_of_strings[i]
    if key not in element:
        list_of_strings.remove(element)
print(list_of_strings)


lines = int(input())
numbers = []
filtered = []

for i in range(lines):
    number = int(input())
    numbers.append(number)
command = input()
if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
print(filtered)