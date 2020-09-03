from euler import utils


class Solution:

    @classmethod
    def get_first_consequent_number(cls, consecutive):
        n = 1
        c = 0
        while True:
            if cls.distinct_count(utils.get_prime_factors(n)) == consecutive:
                c += 1
            else:
                c = 0

            if c == consecutive:
                return n - consecutive + 1

            n += 1

    @classmethod
    def distinct_count(cls, l: list):
        if len(l) == 0:
            return 0
        c = 1
        for i in range(1, len(l)):
            if l[i] != l[i - 1]:
                c += 1
        return c



