import bisect
import unittest


class Solution:

    def reversePairs(self, nums):
        s = 0
        array_sorted = [nums[-1] * 2 + 1]
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            lower = bisect.bisect_right(array_sorted, n)
            s += lower
            bisect.insort_right(array_sorted, n * 2 + 1)
        return s


class SolutionTest(unittest.TestCase):

    def test_reversePairs(self):
        self.assertEquals(Solution().reversePairs([1, 3, 2, 3, 1]), 2)
        self.assertEquals(Solution().reversePairs([2, 4, 3, 5, 1]), 3)
        self.assertEquals(Solution().reversePairs([5, 4, 3, 2, 1]), 4)


