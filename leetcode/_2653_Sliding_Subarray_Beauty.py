import bisect
import unittest
from typing import List


class Solution:

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        neg = 0
        for i in range(0, k - 1):
            neg += nums[i] < 0
        ref = sorted(nums[0:k])
        for i in range(0, len(nums) - k + 1):
            if i > 0:
                neg -= nums[i - 1] < 0
                to_rem = bisect.bisect_left(ref, nums[i - 1])
                del ref[to_rem]
                bisect.insort(ref, nums[i + k - 1])
            neg += nums[i + k - 1] < 0
            if neg >= x:
                result.append(ref[x - 1])
            else:
                result.append(0)
        return result


class SolutionTest(unittest.TestCase):

    def test_getSubarrayBeauty(self):
        self.assertEqual(Solution().getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2), [-1, -2, -2])
        self.assertEqual(Solution().getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2), [-1, -2, -3, -4])
        self.assertEqual(Solution().getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1), [-3, 0, -3, -3, -3])


