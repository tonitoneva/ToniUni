n = int(input())

el = set()
for _ in range(n):
    elements = input().split()
    el = el.union(elements)

for element in el:
    print(element)