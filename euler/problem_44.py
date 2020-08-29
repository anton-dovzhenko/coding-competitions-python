import sys


class Solution:

    @classmethod
    def get_min_pentagon_distance(cls):
        pentagons = set()
        d = sys.maxsize
        i = 1
        while i < 10000:
            pentagon = int(i * (3 * i - 1) / 2)
            for p in pentagons:
                if pentagon - p in pentagons and ((1 + (1 + 24 * (pentagon + p)) ** 0.5) / 6).is_integer():
                    print(pentagon - p)
                    d = min(d, pentagon - p)
            pentagons.add(pentagon)
            i += 1
        return d


print(Solution().get_min_pentagon_distance())


