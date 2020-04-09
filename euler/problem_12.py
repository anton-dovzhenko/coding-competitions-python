import math


class Solution:

    def get_highly_divisible_triangular_number(self, n):
        divs = 0
        i = 2
        t = 1
        while divs < n:
            t += i
            i += 1
            divs = 0
            for j in range(1, 1 + math.floor(t ** 0.5)):
                if t % j == 0:
                    divs += 2
        return t

