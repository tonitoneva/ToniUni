a1 = int(input())
b = int(input())
print(f"Before:\na = {a1}\nb = {b}")
a = b
b = a1
print(f"After:\na = {a}\nb = {b}")

first = input()
second = input()
third = input()

list = [ third, second, first]
print(list)

n = int(input())
courses = []

for i in range(n):
    current_course = input()
    courses.append(current_course)
print(courses)

numbers = int(input())
positive = []
negative = []

for i in range(numbers):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
print(f"{positive}\n{negative}\nCount of positives: {len(positive)}\nSum of negatives: {sum(negative)}")