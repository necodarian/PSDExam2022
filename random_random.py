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
        a = (max_range - min_range)
        if type(amount) is str:
            raise ValueError("No valid integer!")

        if min_range >= max_range:
            raise ValueError(f"It is required that {max_range} should be higher than {min_range}!")

        elif amount > a:
            raise ValueError(f"The total generated numbers must be lower than the length of range({min_range}, {max_range})!")

        else:
            random_list = random.sample(range(min_range, max_range), amount)
            print(random_list)
            print(f"The data types of random_list items are {type(random_list[0])}")
            print(f"The length of random_list {len(random_list)} is lower than the length of the range between min_range and max_range{a}")



RandomNumber.random_number(5, 1, 20)


