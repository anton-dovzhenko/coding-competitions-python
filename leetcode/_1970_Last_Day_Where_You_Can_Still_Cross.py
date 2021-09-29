import unittest

import numpy


class Solution:

    def bfs(self, row, col, visited, nodes):
        next_nodes = []
        for n in nodes:
            for inc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nn = (n[0] + inc[0], n[1] + inc[1])
                if (0 <= nn[0] < row) and (0 <= nn[1] < col) and visited[nn] == 0:
                    if nn[0] == row - 1:
                        return True
                    next_nodes.append(nn)
                    visited[nn] = 1
        if len(next_nodes) == 0:
            return False

        return self.bfs(row, col, visited, next_nodes)

    def can_cross(self, row, col, cells, m):
        visited = numpy.zeros((row, col))
        nodes = []
        for i in range(m):
            c = cells[i]
            visited[(c[0] - 1, c[1] - 1)] = 1
        for i in range(col):
            if visited[(0, i)] == 0:
                nodes.append([0, i])
            visited[(0, i)] = 1
        return self.bfs(row, col, visited, nodes)

    def latestDayToCross(self, row, col, cells):
        left = 0
        right = len(cells)
        m = 0
        while left < right:
            m = (left + right) // 2
            flag = self.can_cross(row, col, cells, m)
            if flag:
                left += 1
            else:
                right -= 1
        return m


class SolutionTest(unittest.TestCase):

    def test_latestDayToCross(self):
        self.assertEquals(Solution().latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]), 2)
        self.assertEquals(Solution().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]), 1)
        self.assertEquals(Solution().latestDayToCross(
            3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]), 3)
        self.assertEquals(Solution().latestDayToCross(
            6, 2, [[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2], [1, 2]]), 3)

