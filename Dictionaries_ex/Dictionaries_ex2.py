list = []
list_of_words = []
list_of_numbers = []
dictionary_word_number = {}

words = input()
while words != "stop":
    list.append(words)
    words = input()

counter1 = 1
for item in list:
    if counter1 % 2 == 1:
        list_of_words.append(item)
    else:
        list_of_numbers.append(item)
    counter1 += 1

for item in list_of_words:
    if item in dictionary_word_number.keys():
        dictionary_word_number[item] += int(list_of_numbers[0])
        del list_of_numbers[0]
    else:
        dictionary_word_number[item] = int(list_of_numbers[0])
        del list_of_numbers[0]

for key, value in dictionary_word_number.items():
    print(f"{key} -> {value}")





