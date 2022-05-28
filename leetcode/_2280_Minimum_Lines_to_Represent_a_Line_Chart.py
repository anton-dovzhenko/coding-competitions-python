import unittest
from fractions import Fraction
from typing import List


class Solution:

    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        lines = set()
        for i in range(len(stockPrices) - 1):
            p1 = stockPrices[i]
            p2 = stockPrices[i + 1]
            alpha = Fraction(p2[1] - p1[1], p2[0] - p1[0])
            beta = Fraction(p1[1] * (p2[0] - p1[0]) - (p2[1] - p1[1]) * p1[0], p2[0] - p1[0])
            lines.add((alpha, beta))
        return len(lines)


class SolutionTest(unittest.TestCase):

    def test_latestDayToCross(self):
        self.assertEqual(Solution().minimumLines([[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]), 3)
        self.assertEqual(Solution().minimumLines([[3, 4], [1, 2], [7, 8], [2, 3]]), 1)
        self.assertEqual(
            Solution().minimumLines([[1, 1000000000], [1000000000, 1000000000], [999999999, 1], [2, 999999999]]), 3)
        self.assertEqual(Solution().minimumLines([[72, 98], [62, 27], [32, 7], [71, 4], [25, 19], [91, 30], [52, 73],
                                                  [10, 9], [99, 71], [47, 22], [19, 30], [80, 63], [18, 15], [48, 17],
                                                  [77, 16], [46, 27], [66, 87], [55, 84], [65, 38], [30, 9], [50, 42],
                                                  [100, 60], [75, 73], [98, 53], [22, 80], [41, 61], [37, 47],
                                                  [95, 8], [51, 81], [78, 79], [57, 95]]), 29)
        self.assertEqual(Solution().minimumLines([[1, 2], [8, 31], [15, 60]]), 1)
