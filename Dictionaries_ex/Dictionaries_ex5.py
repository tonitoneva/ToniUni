import operator
from collections import OrderedDict

materials = {}
while True:
    gamer_input = input().lower().split(" ")
    for x in range(len(gamer_input)):
        if gamer_input[1] not in materials.keys():
            materials[gamer_input[1]]=gamer_input[0]
            gamer_input.remove(gamer_input[0])
            gamer_input.remove(gamer_input[1])
            if gamer_input[1] == "shards" and int(gamer_input[0]) >= 250:
                materials["shards"] -= 250
                print(f"Shadowmourne obtained!")
                sort_val_d = OrderedDict(sorted(materials.items(), key=operator.itemgetter(1), reverse=True))
                for y in range(len(materials)):
                    if sort_val_d[y] == "shards" or sort_val_d[y] == "motes" or sort_val_d[y] == "fragments":
                        print(f"{sort_val_d[y]}: {sort_val_d.get(sort_val_d[y])}")
                        

        else:
            materials[gamer_input[1]] += gamer_input[0]
            gamer_input.remove(gamer_input[0])
            gamer_input.remove(gamer_input[1])

