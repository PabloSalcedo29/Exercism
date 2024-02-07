def square(number):
    if number > 0 and number < 65:
        grains = 2 ** (number - 1)
        return grains
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    n = 1
    sum_grains = 0
    while n <= 64:
        grains = 2 ** (n - 1)
        n += 1
        sum_grains += grains
    return sum_grains

