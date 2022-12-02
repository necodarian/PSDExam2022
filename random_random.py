import random


class RandomNumber:

    @classmethod
    def random_number(cls, amount: int, min_range:int, max_range: int):
        """
        Generating one or more random numbers based on given properties.
        Args:
            amount: Integer numbers that will be returned.
            min_range: starting range of the random number(integer).
            max_range: maximum number(integer) the random number can be.

        Returns:
            A list of numbers(integers) according to the amount
        """

