from euler import utils


class Solution:

    @classmethod
    def get_consecutive_prime_sum(cls, N):
        length = 0
        result = 0
        primes = utils.get_primes(N)
        s_primes = set(primes)

        for i in range(1, len(primes)):
            primes[i] += primes[i - 1]
        primes.insert(0, 0)

        for st in range(0, len(primes) - 1):
            for end in range(st + 1, len(primes)):
                p = primes[end] - primes[st]
                if p > N:
                    break
                if p in s_primes:
                    if end - st > length:
                        length = end - st
                        result = p

        return result

