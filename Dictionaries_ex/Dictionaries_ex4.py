name_book = {}
number_of_searches = 0
while True:
    userInput = input()
    if not userInput.isdigit():
        name_list = userInput.split("-")
        name_book[name_list[0]] = name_list[1]
    else:
        number_of_searches = int(userInput)
        break

for x in range(0, number_of_searches):
    userInput = input()
    if userInput in name_book.keys():
        print(f"{userInput} -> {name_book.get(userInput)}")
    else:
        print(f"Contact {userInput} does not exist.")




