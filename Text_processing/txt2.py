string = input().split(" ")
result = ""
for word in string:
    lenght = len(word)
    result += word * lenght
print(result)