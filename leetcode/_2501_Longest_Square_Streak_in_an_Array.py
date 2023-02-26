import unittest
from typing import List


class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = -1
        for num in nums:
            n = num
            temp = 1
            while (n := n ** 2) in nums:
                temp += 1
                longest = max(longest, temp)

        return longest


class SolutionTest(unittest.TestCase):

    def test_longestSquareStreak(self):
        self.assertTrue(Solution().longestSquareStreak([4, 3, 6, 16, 8, 2]), 3)
        self.assertTrue(Solution().longestSquareStreak([2, 3, 5, 6, 7]), -1)


