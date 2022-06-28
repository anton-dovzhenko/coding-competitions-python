import unittest
from typing import List


class Solution:

    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                a = grid[i][j]
                diag = i == j or i + j == n - 1
                if diag and a == 0 or not diag and a != 0:
                    return False
        return True


class SolutionTest(unittest.TestCase):

    def test_calculateTax(self):
        self.assertTrue(Solution().checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
        self.assertFalse(Solution().checkXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]]))
