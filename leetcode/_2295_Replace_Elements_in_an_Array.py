import unittest
from typing import List


class Solution:

    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]] = i
        for i, j in operations:
            nums_map[j] = nums_map[i]
            del nums_map[i]
            nums[nums_map[j]] = j
        return nums


class SolutionTest(unittest.TestCase):

    def test_maximumBags(self):
        self.assertEqual(Solution().arrayChange([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]), [3, 2, 7, 1])
        self.assertEqual(Solution().arrayChange([1, 2], [[1, 3], [2, 1], [3, 2]]), [2, 1])
