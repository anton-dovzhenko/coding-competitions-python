from euler import utils


class Solution:

    def sum_non_abudant_sums(self, n):
        abundant = set()
        s = 0
        for i in range(1, n):
            not_sum_of_two = True
            for a in abundant:
                if i - a in abundant:
                    not_sum_of_two = False
                    break
            if not_sum_of_two:
                s += i
            if utils.sum_factors(i) > i:
                abundant |= {i}
        return s


