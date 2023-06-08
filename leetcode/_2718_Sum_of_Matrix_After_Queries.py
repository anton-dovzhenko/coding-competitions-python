import unittest
from typing import List


class Solution:

    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        cols = set()
        rows = set()
        msum = 0
        for q in reversed(queries):
            if q[0] == 0 and q[1] not in rows:
                rows.add(q[1])
                msum += q[2] * (n - len(cols))
            if q[0] == 1 and q[1] not in cols:
                cols.add(q[1])
                msum += q[2] * (n - len(rows))
        return msum


class SolutionTest(unittest.TestCase):

    def test_matrixSumQueries(self):
        self.assertEqual(Solution().matrixSumQueries(3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]), 23)
        self.assertEqual(Solution().matrixSumQueries(3, [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]), 17)
        self.assertEqual(
            Solution().matrixSumQueries(8, [[0, 6, 30094], [0, 7, 99382], [1, 2, 18599], [1, 3, 49292], [1, 0, 81549], [1, 1, 38280], [0, 0, 19405], [0, 4, 30065], [1, 4, 60826],
                                            [1, 5, 9241], [0, 5, 33729], [0, 1, 41456], [0, 2, 62692], [0, 3, 30807], [1, 7, 70613], [1, 6, 9506], [0, 5, 39344], [1, 0, 44658],
                                            [1, 1, 56485], [1, 2, 48112], [0, 6, 43384]]), 22783119)
