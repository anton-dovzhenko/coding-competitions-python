import itertools
import sys

from euler import utils


class Solution:

    @classmethod
    def get_min_prime_pair(cls, N):
        lowest_sum = sys.maxsize
        n = 100_000
        primes = utils.get_primes(n)
        primes_set = set(primes)
        pair_matrix = n * [n * [False]]

        pair_matrix = []
        for i in range(0, 1000):
            pair_matrix.append(1000 * [False])

        for i1 in range(0, 1000):
            for i2 in range(i1 + 1, 1000):
                if cls.is_prime_pairs(primes_set, primes[i1], primes[i2]):
                    pair_matrix[i1][i2] = True
                    pair_matrix[i2][i1] = True

        for i in range(0, 1000):
            lowest_sum = min(lowest_sum, cls._check_next_pair(N - 1, primes, pair_matrix, [i]))

        return lowest_sum

    @classmethod
    def is_prime_pairs(cls, primes_set, n1, n2):
        return int(str(n1) + str(n2)) in primes_set and int(str(n2) + str(n1)) in primes_set

    @classmethod
    def _check_next_pair(cls, N, primes, pair_matrix, pairs):
        if N == 0:
            result = [primes[i] for i in pairs]
            print(result)
            return sum(result)

        flags = pair_matrix[pairs[-1]]
        for i in range(0, len(flags)):
            if flags[i] and i not in pairs:
                all_prime_pairs = True
                for j in pairs:
                    if not pair_matrix[i][j]:
                        all_prime_pairs = False
                        break
                if all_prime_pairs:
                    return cls._check_next_pair(N - 1, primes, pair_matrix, pairs + [i])
                else:
                    return sys.maxsize

        return sys.maxsize

# primes = utils.get_primes(10000)
# primes_set = set(primes)
# print(Solution.is_prime_pairs(primes_set, 2, 3))


print(Solution.get_min_prime_pair(4))



# primes_set = set(utils.get_primes(10_0000))
# print(Solution.is_prime_pairs(primes_set, [3, 7, 109, 673]))

# print(list(itertools.combinations(range(10), 5)))
#
# print(sum([2, 5, 99]))
# print([2, 6] + [7])


