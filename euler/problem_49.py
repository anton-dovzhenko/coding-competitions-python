from euler import utils


class Solution:

    @classmethod
    def get_prime_permutations(cls):
        primes = utils.get_primes(10_000)
        d = {}
        for p in primes:
            if 1000 < p < 10_000:
                key = ''.join(sorted(str(p)))
                if key not in d:
                    d[key] = list()
                d[key].append(p)

        triplets = []
        for key, value in d.items():
            if len(value) > 2:
                for i1 in range(0, len(value)):
                    for i2 in range(i1 + 1, len(value)):
                        if (2 * value[i2] - value[i1]) in value:
                            triplets.append("%s%s%s" % (value[i1], value[i2], 2 * value[i2] - value[i1]))

        return triplets

