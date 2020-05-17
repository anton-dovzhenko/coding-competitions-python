import math


class Solution:

    prime_cache: set = set()

    @classmethod
    def get_quadratic_primes(cls, a, b):
        max_n = 0
        product = None
        for i in range(-1 * a, a):
            for j in range(-b, b + 1):
                n = 0
                while cls._is_prime(n * n + i * n + j):
                    n += 1

                if n > max_n:
                    max_n = n
                    product = i * j

        return product

    @classmethod
    def _is_prime(cls, n):
        if n < 0:
            return False
        if n in cls.prime_cache:
            return True
        for i in range(2, int(math.ceil(n ** 0.5))):
            if n % i == 0:
                return False
        cls.prime_cache.add(n)
        return True

