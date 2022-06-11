import unittest
from typing import List


class Solution:

    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        new_nums = []
        for i in range(int(n / 2)):
            if i % 2 == 0:
                new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                new_nums.append(max(nums[2 * i], nums[2 * i + 1]))

        return self.minMaxGame(new_nums)


class SolutionTest(unittest.TestCase):

    def test_maximumBags(self):
        self.assertEqual(Solution().minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]), 1)
        self.assertEqual(Solution().minMaxGame([3]), 3)


