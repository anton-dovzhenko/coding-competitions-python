import unittest
from typing import List


class Solution:

    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        pc = 0  # pc is partition count
        start = - 1 - k
        for n in nums:
            if n - start > k:
                pc += 1
                start = n
        return pc


class SolutionTest(unittest.TestCase):

    def test_maximumBags(self):
        self.assertEqual(Solution().partitionArray([3, 6, 1, 2, 5], 2), 2)
        self.assertEqual(Solution().partitionArray([1, 2, 3], 1), 2)
        self.assertEqual(Solution().partitionArray([2, 2, 4, 5], 0), 3)


