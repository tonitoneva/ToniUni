numbers = input().split()
new_numbers = []
for number in range(len(numbers)):
    new_number = (int(numbers[number]))
    new_numbers.append(new_number)

command_input =input()
while command_input != "Finish":
    command_args = command_input.split(" ")
    command = command_args[0]
    value = int(command_args[1])

    if command == "Add":
        new_numbers.append(value)
    elif command == "Remove":
        if value in new_numbers:
            new_numbers.remove(value)
    elif command == "Replace":
        second_value = int(command_args[2])
        for i in range(len(new_numbers)):
            if (new_numbers[i] == value):
                new_numbers[i] = second_value
                break
    elif command == "Collapse":
        new_numbers =[x for x in new_numbers if x >= value]
    command_input = input()

print(*new_numbers, sep = " ")

