#latin alphabet
number = int(input())
stat = 97
end = 97 + number

for first_char in range(stat, end):
    for second_char in range(stat, end):
        for third_char in range(stat, end):
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")
#from int to char
first_number = int(input())
last_number = int(input())
for i in range(first_number,last_number +1):
    print(f"{chr(i)} ", end="")

#water flow
lines = int(input())
for n in range(lines):
    next = 0
    next += int(input())
if next < 255:
    print(f"Insufficient capacity! {next}")





