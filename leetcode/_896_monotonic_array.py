import unittest


class Solution:

    def isMonotonic(self, A):
        pos = 0
        neg = 0
        for i in range(0, len(A) - 1):
            d = A[i + 1] - A[i]
            if d < 0:
                neg += 1
            elif d > 0:
                pos += 1
            if not pos * neg == 0:
                return False

        return pos * neg == 0


class SolutionTest(unittest.TestCase):

    def test_isMonotonic(self):
        self.assertTrue(Solution().isMonotonic([1, 2, 2, 3]))
        self.assertTrue(Solution().isMonotonic([6, 5, 4, 4]))
        self.assertFalse(Solution().isMonotonic([1, 3, 2]))


