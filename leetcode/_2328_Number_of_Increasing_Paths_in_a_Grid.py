import unittest
from functools import lru_cache
from typing import List


class Solution:

    MOD = 10 ** 9 + 7
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def countPaths(self, grid: List[List[int]]) -> int:
        count = 0

        @lru_cache(None)
        def count_path(i, j):
            result = 1
            for d in self.DIRS:
                i_next = i + d[0]
                j_next = j + d[1]
                if 0 <= i_next < len(grid) and 0 <= j_next < len(grid[0]) and grid[i_next][j_next] > grid[i][j]:
                    result += count_path(i_next, j_next)
            result %= self.MOD
            return result

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = (count + count_path(i, j)) % self.MOD
        return count


class SolutionTest(unittest.TestCase):

    def test_countPaths(self):
        self.assertEqual(Solution().countPaths([[1, 1], [3, 4]]), 8)
        self.assertEqual(Solution().countPaths([[1], [2]]), 3)

