import math
from collections import Counter
from itertools import permutations

import numpy


class Solution:

    @classmethod
    def get_digit_cancelling_fractions(cls):
        numerators = []
        denominators = []
        for i in range(10, 100):
            for j in range(i + 1, 100):
                if j % 10 == 0 or i % 10 == i // 10 or j % 10 == j // 10:
                    continue
                n1 = str(i)
                n2 = str(j)
                c = Counter(n1 + n2)
                if len(c) == 3:
                    digit = c.most_common(1)[0][0]
                    n1 = n1.replace(digit, '')
                    n2 = n2.replace(digit, '')
                    if abs(i / j - int(n1) / int(n2)) < 1e-6:
                        print(i, j)
                        numerators.append(i)
                        denominators.append(j)
        n = numpy.prod(numerators)
        d = numpy.prod(denominators)
        return d // numpy.gcd(n, d)

