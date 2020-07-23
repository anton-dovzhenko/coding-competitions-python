import math


class Solution:

    @classmethod
    def get_truncatable_primes(cls, N):
        s = 0
        s_count = 0
        primes = [2]
        i = primes[-1]
        while s_count < N:
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
                if cls.is_truncateable(primes, i):
                    s += i
                    s_count += 1
            i += 1

        return s

    @classmethod
    def is_truncateable(cls, primes, n):
        if n <= 7:
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes or int(s[0:i]) not in primes:
                return False
        return True

