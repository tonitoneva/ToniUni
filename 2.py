import math

procesori= int(input())
rabotnici = int(input())
days = int(input())

hours = rabotnici * days * 8
procesori_for_hour = math.floor(hours / 3)

if procesori_for_hour >= procesori:
    print(f"Profit: ->{(procesori_for_hour - procesori) * 110.10: .2f} BGN")
else:
    print(f"Losses: ->{(procesori - procesori_for_hour) * 110.10: .2f} BGN")
