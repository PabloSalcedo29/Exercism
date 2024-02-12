def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    n = 1
    sum_div = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    while n <= (number / 2):
        if number % n == 0:
            sum_div += n
            n += 1
        else:
            n += 1


    if sum_div == number:
        return "perfect"
    if sum_div < number:
        return "deficient"
    if sum_div > number:
        return "abundant"