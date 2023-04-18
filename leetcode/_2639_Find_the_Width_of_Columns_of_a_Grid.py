import unittest
from typing import List


class Solution:

    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        widths = [0] * len(grid[0])
        for j in range(0, len(grid[0])):
            for i in range(0, len(grid)):
                widths[j] = max(widths[j], len(str(grid[i][j])))
        return widths


class SolutionTest(unittest.TestCase):

    def test_findColumnWidth(self):
        self.assertEqual(Solution().findColumnWidth([[1], [22], [333]]), [3])
        self.assertEqual(Solution().findColumnWidth([[-10], [3], [12]]), [3])
        self.assertEqual(Solution().findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]), [3, 1, 2])



