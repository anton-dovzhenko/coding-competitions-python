import itertools
import unittest
from typing import List


# brute-force
class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        best = float('inf')
        n = len(cookies)
        if n == k:
            return max(cookies)

        options = [list(range(k))] * n
        for partition in itertools.product(*options):
            if all(item in partition for item in range(k)):
                sums = dict(zip(range(n), [0] * n))
                for i in range(n):
                    sums[partition[i]] += cookies[i]
                best = min(best, max(sums.values()))

        return best


class SolutionTest(unittest.TestCase):

    def test_calculateTax(self):
        self.assertEqual(Solution().distributeCookies([8, 15, 10, 20, 8], 2), 31)
        self.assertEqual(Solution().distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3), 7)
        self.assertEqual(Solution().distributeCookies([13, 3], 2), 13)
        self.assertEqual(Solution().distributeCookies([76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609], 8),
                         76265)
