import unittest
from collections import Counter


class Solution:

    def findLucky(self, arr):
        frequency = Counter(arr)
        match = -1
        for k, v in frequency.items():
            if k == v:
                match = max(match, k)
        return match


class SolutionTest(unittest.TestCase):

    def test_findLucky(self):
        self.assertEqual(Solution().findLucky([2, 2, 3, 4]), 2)
        self.assertEqual(Solution().findLucky([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(Solution().findLucky([2, 2, 2, 3, 3]), -1)
        self.assertEqual(Solution().findLucky([5]), -1)
        self.assertEqual(Solution().findLucky([7, 7, 7, 7, 7, 7, 7]))


