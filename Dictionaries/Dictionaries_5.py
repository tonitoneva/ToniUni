list_of_characters = input().split(", ")
dictonary = {}

for char in list_of_characters:
    dictonary[char] = ord(char)
print(dictonary)