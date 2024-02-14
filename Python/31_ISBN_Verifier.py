def is_valid(isbn):
    counter = 10
    result = 0
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    for num in isbn:
        if num == '-':
            continue
        if num.isdigit():
            result += (int(num) * counter)
            counter -= 1
            continue
        if num == 'X' and counter == 1:
            result += (10 * counter)
            counter -= 1
            continue

        else:
            return False

    return counter == 0 and result % 11 == 0

