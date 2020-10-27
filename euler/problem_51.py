import itertools
from euler import utils


class Solution:

    @classmethod
    def get_prime_digit_replacements(cls, n, target):
        primes = utils.get_primes(n)
        primes = [str(x) for x in primes]
        primes_set = set(primes)
        numbers = [chr(ord('0') + x) for x in range(10)]
        for p in primes:
            for replace_count in range(1, len(p)):
                for rplc in set(itertools.combinations(range(len(p)), replace_count)):
                    if not cls._is_same(p, rplc):
                        continue
                    prime_count = 0
                    for n in numbers:
                        if cls._replace(p, n, rplc) in primes_set:
                            prime_count += 1
                    if prime_count == target:
                        # print("prime=%s, prime_count=%s" % (p, prime_count))
                        return int(p)

    @classmethod
    def _is_same(cls, seq, indices):
        x = seq[indices[0]]
        for i in range(1, len(indices)):
            if seq[indices[i]] != x:
                return False
        return True

    @classmethod
    def _replace(cls, s, c, indices):
        result = ''
        for i in range(len(s)):
            result += c if i in indices else s[i]
        return result

