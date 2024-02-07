def equilateral(sides):
    a, b, c = sides
    while a > 0 or b > 0 or c > 0:
        if (a + b >= c) and (a + c >= b) and (c + b >= a):
            if (a == b) and (b == c) and (a == c):
                return True
            else:
                return False
        else:
            return False
    return False

def isosceles(sides):
    a, b, c = sides
    while a > 0 or b > 0 or c > 0:
        if (a + b >= c) and (a + c >= b) and (c + b >= a):
            if (a == b) or (b == c) or (a == c):
                return True
            else:
                return False
        else:
            return False
    return False


def scalene(sides):
    a, b, c = sides
    while a > 0 or b > 0 or c > 0:
        if (a + b >= c) and (a + c >= b) and (c + b >= a):
            if (a != b) and (b != c) and (a != c):
                return True
            else:
                return False
        else:
            return False
    return False
