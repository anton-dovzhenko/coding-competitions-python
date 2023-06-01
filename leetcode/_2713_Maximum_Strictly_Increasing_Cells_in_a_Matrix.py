import collections
import unittest
from typing import List


class Solution:

    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        M = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                points = []
                if mat[i][j] in M:
                    points = M[mat[i][j]]
                else:
                    M[mat[i][j]] = points
                points.append((i, j))
        M = collections.OrderedDict(sorted(M.items()))

        for key in M:
            next_value = []
            points = M[key]
            for point in points:
                next_value.append(1 + max(rows[point[0]], cols[point[1]]))
            for i in range(len(points)):
                rows[points[i][0]] = max(rows[points[i][0]], next_value[i])
                cols[points[i][1]] = max(cols[points[i][1]], next_value[i])

        return max(max(rows), max(cols))


class SolutionTest(unittest.TestCase):

    def test_maxIncreasingCells(self):
        self.assertEqual(Solution().maxIncreasingCells([[3, 1], [3, 4]]), 2)
        self.assertEqual(Solution().maxIncreasingCells([[1, 1], [1, 1]]), 1)
        self.assertEqual(Solution().maxIncreasingCells([[3, 1, 6], [-9, 5, 7]]), 4)


