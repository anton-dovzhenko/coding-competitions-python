import math



class Solution:

    def get_prime(self, n):
        primes = []
        i = 2
        while len(primes) < n:
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
            i += 1
        return primes[-1]

