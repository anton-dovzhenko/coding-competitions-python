import bisect
import unittest


class Solution:

    def countSmaller(self, nums):
        counts = [0]
        array_sorted = [nums[-1] + 1]
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            lower = bisect.bisect_right(array_sorted, n)
            counts.append(lower)
            bisect.insort_right(array_sorted, n + 1)
        counts.reverse()
        return counts


class SolutionTest(unittest.TestCase):

    def test_countSmaller(self):
        self.assertEquals(Solution().countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])
        self.assertEquals(Solution().countSmaller([-1]), [0])
        self.assertEquals(Solution().countSmaller([-1, -1]), [0, 0])



