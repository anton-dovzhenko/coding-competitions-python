import unittest
from typing import List


class Solution:

    def semiOrderedPermutation(self, nums: List[int]) -> int:
        i1 = nums.index(1)
        i2 = nums.index(len(nums))
        return i1 + (len(nums) - 1 - i2) - (i1 > i2)


class SolutionTest(unittest.TestCase):

    def test_semiOrderedPermutation(self):
        self.assertEqual(Solution().semiOrderedPermutation([2, 1, 4, 3]), 2)
        self.assertEqual(Solution().semiOrderedPermutation([2, 4, 1, 3]), 3)
        self.assertEqual(Solution().semiOrderedPermutation([1, 3, 4, 2, 5]), 0)


