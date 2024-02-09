def steps(number):
    n_steps = 0
    n = number
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while n != 1:
        if n % 2 == 0:
            n = n/2
            n_steps += 1

        else:
            n = 3*n + 1
            n_steps += 1
    return n_steps


