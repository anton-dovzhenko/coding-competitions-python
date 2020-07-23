import math


class Solution:

    @classmethod
    def get_circular_primes(cls, N):
        primes = [2]
        i = primes[-1]
        while i < N:
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

        primes = set(primes)

        cnt = 0
        for p in primes:
            L = int(math.log10(p)) + 1
            circular = True
            for i in range(1, L):
                p = (p % 10) * 10 ** (L - 1) + p // 10
                if p not in primes:
                    circular = False
                    break
            if circular:
               cnt += 1

        return cnt

