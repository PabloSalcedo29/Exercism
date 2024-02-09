import math
def score(x, y):
    dist = math.sqrt((x ** 2) + (y ** 2))
    if dist <= 1:
        return 10
    if dist <= 5:
        return 5
    if dist <= 10:
        return 1
    else:
        return 0
