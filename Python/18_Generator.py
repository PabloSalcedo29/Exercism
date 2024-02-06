"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ["A", "B", "C", "D"]
    while number > 0:
        for l in letters:
            if number > 0:
                number -= 1
                yield l
            else:
                return


def generate_seats(num_seats):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    current_seat = 1
    seat_letter_gen = generate_seat_letters(num_seats)
    while num_seats > 0:
        for seat_letter in seat_letter_gen:
            row = (current_seat - 1) // 4 + 1
            if row >= 13:
                row += 1
            yield f"{row}{seat_letter}"
            current_seat += 1
            num_seats -= 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    dict_pass = {}
    seat_number = generate_seats(len(passengers))
    for name, seat in zip(passengers, seat_number):
        dict_pass[name] = seat
    return dict_pass


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        n_zeros = 12 - len(flight_id) - len(seat)
        yield f"{seat}{flight_id}{'0' * n_zeros}"
