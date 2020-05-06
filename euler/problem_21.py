from euler import utils


class Solution:

    def sum_amicable_numbers(self, n):
        s = 0
        d = {}
        for i in range(1, n):
            d[i] = utils.sum_factors(i)

        for key, value in d.items():
            if key != value and value in d and d[value] == key:
                s += key + value

        return int(s / 2)

