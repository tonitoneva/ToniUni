kids = 0
adults = 0

line = input()

while (line != "Christmas"):
    if int(line) <= 16:
        kids += 1
    elif int(line) > 16:
        adults += 1
    line = input()

sum_for_toys = kids * 5
sum_for_adults = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {sum_for_toys}")
print(f"Money for sweaters: {sum_for_adults}")
