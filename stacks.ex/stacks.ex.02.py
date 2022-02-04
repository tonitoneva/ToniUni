n = int(input())
list_of_int = []
for _ in range(n):
    line_parts = input().split()
    command = line_parts[0]

    if command == "1":
        list_of_int.append(line_parts[1])

    if command == "2" and list_of_int:
        list_of_int.pop()

    if command == "3" and list_of_int:
        print(max(list_of_int))

    if command == "4" and list_of_int:
        print(min(list_of_int))
list_of_int.reverse()
print(", ".join(list_of_int))
