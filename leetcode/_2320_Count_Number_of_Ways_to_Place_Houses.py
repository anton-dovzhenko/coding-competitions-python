import sys
import unittest

sys.setrecursionlimit(10 ** 4 + 1)


class Solution:

    M = 10 ** 9 + 7

    def countHousePlacements(self, n: int) -> int:
        cache0 = {}
        cache1 = {}
        lc = self.count_layouts(0, n, cache0, cache1)
        return (lc * lc) % self.M

    def count_layouts(self, last, n, cache0, cache1):
        if n == 0:
            return 1
        if n - 1 not in cache0:
            cache0[n - 1] = self.count_layouts(0, n - 1, cache0, cache1)
        result = cache0[n - 1]
        if last == 0:
            if n - 1 not in cache1:
                cache1[n - 1] = self.count_layouts(1, n - 1, cache0, cache1)
            result += cache1[n - 1]
        return result

    def countHousePlacements2(self, n: int) -> int:
        f1 = 1
        f2 = 2
        for i in range(2, n + 1):
            f1, f2 = f2, f1 + f2
        return (f2 * f2) % self.M


class SolutionTest(unittest.TestCase):

    def test_countHousePlacements(self):
        self.assertEqual(Solution().countHousePlacements(1), 4)
        self.assertEqual(Solution().countHousePlacements(2), 9)
        self.assertEqual(Solution().countHousePlacements(3), 25)
        self.assertEqual(Solution().countHousePlacements(1000), 500478595)

    def test_countHousePlacements2(self):
        self.assertEqual(Solution().countHousePlacements2(1), 4)
        self.assertEqual(Solution().countHousePlacements2(2), 9)
        self.assertEqual(Solution().countHousePlacements2(3), 25)
        self.assertEqual(Solution().countHousePlacements2(1000), 500478595)


