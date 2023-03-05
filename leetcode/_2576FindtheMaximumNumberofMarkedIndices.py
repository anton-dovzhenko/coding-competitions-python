import unittest
from typing import List


class Solution:

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) // 2
        marked = 0
        while j < len(nums):
            if nums[i] > 0 and nums[j] >= 2 * nums[i]:
                marked += 2
                nums[j] = -1
                i += 1
                j += 1
            else:
                j += 1

        return marked


class SolutionTest(unittest.TestCase):

    def test_maxNumOfMarkedIndices(self):
        self.assertEqual(Solution().maxNumOfMarkedIndices([3, 5, 2, 4]), 2)
        self.assertEqual(Solution().maxNumOfMarkedIndices([9, 2, 5, 4]), 4)
        self.assertEqual(Solution().maxNumOfMarkedIndices([7, 6, 8]), 0)
