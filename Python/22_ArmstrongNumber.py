def is_armstrong_number(number):
    sum_total = 0
    for digit in str(number):
        sum_total = sum_total + (int(digit) ** len(str(number)))
    return sum_total == number
