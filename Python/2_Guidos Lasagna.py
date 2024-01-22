"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

def preparation_time_in_minutes(layers):
    """Calculate the bake time needed for the layers.

    :param layers: int - lasagna layers.
    :return: int - total bake time (in minutes) derived from the layers of the lasagna.

    Function that takes the layers of the lasgana and calculates the time needed. 2 minutes per layer. Returns the preparation_time
    """
    preparation_time = layers * 2
    return preparation_time


def elapsed_time_in_minutes(capas, tiempo):
    """Calculate the bake time completed.

    :param tiempo: int - baking time already elapsed.
    :param capas: int - lasagna layers.
    :return: int -  end_time. Time the lasagana has already spent in the oven (in minutes).

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and the layers of the lasgna and returns how many minutes the lasagna has been in the oven.
    """
    end_time = tiempo + (2*capas)
    return end_time
