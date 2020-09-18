import itertools


class Solution:

    @classmethod
    def get_sum_of_sub_string_divisible_pandigitals(cls):
        s = 0
        divisors = [2, 3, 5, 7, 11, 13, 17]
        for n in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
            if n[0] != 0:
                if cls.is_sub_divisible(divisors, n):
                    s += cls.array_to_number(n)

        return s

    @classmethod
    def is_sub_divisible(cls, divisors, n):
        for i in range(0, 7):
            if cls.array_to_number(n[i + 1: i + 4]) % divisors[i] != 0:
                return False
        return True

    @classmethod
    def array_to_number(cls, a):
        s = 0
        for n in a:
            s = s * 10 + n
        return s
