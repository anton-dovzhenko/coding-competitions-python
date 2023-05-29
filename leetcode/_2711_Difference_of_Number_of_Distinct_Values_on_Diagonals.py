import unittest
from typing import List


class Solution:

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(0, len(grid)):
            result.append([])
            for j in range(0, len(grid[i])):
                top = set()
                bottom = set()
                i0 = i - 1
                j0 = j - 1
                while i0 >= 0 and j0 >= 0:
                    top.add(grid[i0][j0])
                    i0 -= 1
                    j0 -= 1
                i0 = i + 1
                j0 = j + 1
                while i0 < len(grid) and j0 < len(grid[0]):
                    bottom.add(grid[i0][j0])
                    i0 += 1
                    j0 += 1
                result[-1].append(abs(len(top) - len(bottom)))
        return result


class SolutionTest(unittest.TestCase):

    def test_differenceOfDistinctValues(self):
        self.assertEqual(Solution().differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]),
                         [[1, 1, 0], [1, 0, 1], [0, 1, 1]])
