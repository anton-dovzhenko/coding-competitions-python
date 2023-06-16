import unittest
from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) > 2:
            return sorted(nums[0:3])[1]
        return -1


class SolutionTest(unittest.TestCase):

    def test_findNonMinOrMax(self):
        self.assertEqual(Solution().findNonMinOrMax([3, 2, 1, 4]), 2)
        self.assertEqual(Solution().findNonMinOrMax([1, 2]), -1)
        self.assertEqual(Solution().findNonMinOrMax([2, 1, 3]), 2)


