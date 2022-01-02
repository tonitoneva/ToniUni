phones = input().split(", ")
command = input()
new_phones = []
command_arg = []
replacePhoneCommands = []
for i in range(len(phones)):
    phoneToAdd = (phones[i])
    new_phones.append(phoneToAdd)

while command != "End":
    command_arg = command.split(" - ")
    command = command_arg[0]
    string = command_arg[1]

    if command == "Add":
        if string not in new_phones:
            new_phones.append(string)
    if command == "Remove":
        if string in new_phones:
            new_phones.remove(string)
    if command == "Bonus phone":
        string.split(":")
        replacePhoneCommands = command_arg[1].split(":")
        oldPhone = replacePhoneCommands[0]
        newPhone = replacePhoneCommands[1]
        if oldPhone in new_phones:
            new_phones.insert(new_phones.index(oldPhone) +1, newPhone)
    if command == "Last":
        if string in new_phones:
            new_phones.remove(string)
            new_phones.append(string)
    command = input()

print(', '.join(new_phones))

