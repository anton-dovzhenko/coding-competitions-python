import unittest
from collections import Counter


class Solution:

    def minSetSize(self, arr):
        counter = sorted(Counter(arr).values(), reverse=True)
        cum_sum = 0
        size = 0
        thr = len(arr) * 0.5
        for c in counter:
            cum_sum += c
            size += 1
            if cum_sum >= thr:
                return size


class SolutionTest(unittest.TestCase):

    def test_maxValueAfterReverse(self):
        self.assertEquals(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]), 2)
        self.assertEquals(Solution().minSetSize([7, 7, 7, 7, 7, 7]), 1)
        self.assertEquals(Solution().minSetSize([1, 9]), 1)
        self.assertEquals(Solution().minSetSize([1000, 1000, 3, 7]), 1)
        self.assertEquals(Solution().minSetSize([9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]), 5)
