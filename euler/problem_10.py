import math


class Solution:

    def get_sum_of_primes(self, n):
        primes = [2]
        i = primes[-1]
        while i < n:
            i += 1
            root = math.ceil(i ** 0.5)
            is_prime = True
            for p in primes:
                if p > root:
                    break
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
            i += 1
        return sum(primes)

