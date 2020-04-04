from collections import Counter

from euler.utils import get_prime_factors


class Solution:

    def smallest_multiple(self, n):
        sm = 1
        c = Counter()
        for i in range (1, n + 1):
            c |= Counter(get_prime_factors(i))

        for prime in c:
            sm *= prime ** c[prime]

        return sm

