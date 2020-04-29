import math


class Solution:

    def get_factorial_digit_sum(self, n):
        f = 1
        for i in range(2, n + 1):
            f *= i

        s = 0
        for i in str(f):
            s += ord(i) - ord('0')
        return s


