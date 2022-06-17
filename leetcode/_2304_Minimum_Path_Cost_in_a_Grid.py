import unittest
from operator import add
from typing import List


class Solution:

    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        last_cost = grid[0]
        for i in range(1, len(grid)):
            prev_row = grid[i - 1]
            row = grid[i]
            cost = []
            for j in range(len(row)):
                costs = [moveCost[index][j] for index in prev_row]
                cost.append(min(map(add, last_cost, costs)) + row[j])
            last_cost = cost
        return min(last_cost)


class SolutionTest(unittest.TestCase):

    def test_calculateTax(self):
        self.assertEqual(Solution().minPathCost([[5, 3], [4, 0], [2, 1]],
                                                [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]), 17)
        self.assertEqual(Solution().minPathCost([[5, 1, 2], [4, 0, 3]],
                                                [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25],
                                                 [5, 3, 2]]), 6)
