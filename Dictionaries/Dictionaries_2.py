elements = input().split(" ")
shop = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    shop[key] = int(value)

searched_elements = input().split(" ")
for x in range(0, len(searched_elements)):
    second_key = searched_elements[x]
for second_key in searched_elements:
    if second_key in shop:
        print(f"We have {shop[second_key]} of {second_key} left")
    else:
        print(f"Sorry, we don't have {second_key}")

