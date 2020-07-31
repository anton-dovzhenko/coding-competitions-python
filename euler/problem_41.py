import math


#FIXME: very slow
class Solution:

    @classmethod
    def find_largest_pandigital_prime(cls):
        primes = []
        pandigital = 2
        i = 2
        while len(primes) == 0 or primes[-1] <= 7654321:
            is_prime = True
            root = math.ceil(i ** 0.5)
            for p in primes:
                if p > root:
                    break
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
                if cls.is_pandigital(i):
                    pandigital = i
            i += 1
        return pandigital

    @classmethod
    def is_pandigital(cls, n):
        L = int(math.log10(n)) + 1
        c = L * [0]
        while n > 0:
            d = n % 10
            if d == 0 or d > L:
                return False
            c[d - 1] += 1
            if c[d - 1] > 1:
                return False
            n = n // 10
        return True


