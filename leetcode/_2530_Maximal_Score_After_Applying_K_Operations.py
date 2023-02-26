import heapq
import math
import unittest
from typing import List


class Solution:

    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            next_score = -heapq.heappop(nums)
            score += next_score
            heapq.heappush(nums, -math.ceil(next_score / 3.0))
        return score


class SolutionTest(unittest.TestCase):

    def test_longestSquareStreak(self):
        self.assertTrue(Solution().maxKelements([10, 10, 10, 10, 10], 5), 50)
        self.assertTrue(Solution().maxKelements([1, 10, 3, 3, 3], 3), 17)





