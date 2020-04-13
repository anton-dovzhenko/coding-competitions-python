class Solution:

    def get_power_digit_sum(self, n):
        return sum([int(d) for d in str(2 ** n)])

