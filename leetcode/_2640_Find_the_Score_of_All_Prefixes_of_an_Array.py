import unittest
from typing import List


class Solution:

    def findPrefixScore(self, nums: List[int]) -> List[int]:
        nums_max = nums.copy()
        for i in range(1, len(nums_max)):
            nums_max[i] = max(nums_max[i - 1], nums_max[i])
        for i in range(0, len(nums_max)):
            nums_max[i] += nums[i]
        for i in range(1, len(nums_max)):
            nums_max[i] += nums_max[i - 1]
        return nums_max


class SolutionTest(unittest.TestCase):

    def test_findColumnWidth(self):
        self.assertEqual(Solution().findPrefixScore([2, 3, 7, 5, 10]), [4, 10, 24, 36, 56])
        self.assertEqual(Solution().findPrefixScore([1, 1, 2, 4, 8, 16]), [2, 4, 8, 16, 32, 64])




