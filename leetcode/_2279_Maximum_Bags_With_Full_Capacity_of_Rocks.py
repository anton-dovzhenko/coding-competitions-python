import unittest
from typing import List


class Solution:

    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort()
        bags = 0
        for c in capacity:
            if additionalRocks - c >= 0:
                bags += 1
                additionalRocks -= c
            else:
                break
        return bags


class SolutionTest(unittest.TestCase):

    def test_latestDayToCross(self):
        self.assertEqual(Solution().maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2), 3)
        self.assertEqual(Solution().maximumBags([10, 2, 2], [2, 2, 0], 100), 3)

