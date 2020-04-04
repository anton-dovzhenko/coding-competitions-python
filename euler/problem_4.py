from math import floor


class Solution:

    def get_largest_palindrome_product(self, power):
        p = -1
        for i in range(10 ** (power - 1), 10 ** power):
            for j in range(i, 10 ** power):
                n = i * j
                if n == self._reverse_number(n):
                    p = max(p, n)
        return p

    def _reverse_number(self, n):
        r = 0
        while n > 0:
            r = r * 10 + n % 10
            n = floor(n / 10)
        return r

