import sys
import unittest


class Solution:

    def minFallingPathSum(self, grid):
        prev = [0, -1, 0, -1]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not j == prev[1]:
                    grid[i][j] += prev[0]
                else:
                    grid[i][j] += prev[2]
            prev = [sys.maxsize, -1, sys.maxsize, -1]
            for j in range(len(grid[i])):
                n = grid[i][j]
                if n <= prev[0]:
                    prev[2] = prev[0]
                    prev[3] = prev[1]
                    prev[0] = n
                    prev[1] = j
                elif n < prev[2]:
                    prev[2] = n
                    prev[3] = j

        return prev[0]


class SolutionTest(unittest.TestCase):

    def test_minFallingPathSum(self):
        self.assertEquals(Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 13)
        self.assertEquals(Solution().minFallingPathSum([[7]]), 7)
        self.assertEquals(Solution().minFallingPathSum([
            [-73, 61, 43, -48, -36],
            [3, 30, 27, 57, 10],
            [96, -76, 84, 59, -15],
            [5, -49, 76, 31, -7],
            [97, 91, 61, -46, 67]
        ]), -192)



