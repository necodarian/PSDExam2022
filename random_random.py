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
        a = max_range - min_range

        if amount > a:
            raise ValueError(f"The total random number must be lower than the length of range({min_range}, {max_range})!")

        if max_range > min_range:
            random_list = random.sample(range(min_range, max_range), amount)
            print(random_list)
            print(type(random_list[0]))
            print(len(random_list))
