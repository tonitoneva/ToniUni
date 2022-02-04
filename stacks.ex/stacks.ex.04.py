clothes = [int(x) for x in input().split()]
racks = int(input())
counter = 1
current_rack = racks

while clothes:
    current_piece = clothes[-1]
    if current_rack >= current_piece:
        clothes.pop()
        current_rack -= current_piece

    else:
        counter += 1
        current_rack = racks
print(counter)




