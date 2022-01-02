list_of_integers = [int(num) for num in input().split(" ")]
count_of_numbers = int(input())
sorted = list_of_integers
sorted.sort()

for number in range(0, count_of_numbers):
    list_of_integers.remove(sorted[0])
list_of_integers.sort(reverse=True)
print(list_of_integers)


