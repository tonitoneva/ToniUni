area = 0
def areaofRectangle(width, height):
    area = width * height
    return area

width = int(input())
height = int(input())
res = areaofRectangle(width, height)
print(res)