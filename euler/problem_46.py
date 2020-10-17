from euler import utils


class Solution:

    @classmethod
    def get_goldbach_conjecture_min_contradiction(cls, N):
        primes = utils.get_primes(int(N / 2) + 1)
        s_primes = set(primes)
        i = 3
        while i < N:
            if i not in s_primes:
                contradicts = True
                for p in primes:
                    if p >= i:
                        break
                    if (((i - p) / 2) ** 0.5).is_integer():
                        contradicts = False
                        break
                if contradicts:
                    return i
            i += 2


