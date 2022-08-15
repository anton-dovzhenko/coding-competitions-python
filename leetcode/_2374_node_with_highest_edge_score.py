import unittest
from typing import List


class Solution:

    def edgeScore(self, edges: List[int]) -> int:
        score = [0] * len(edges)
        for i in range(len(edges)):
            score[edges[i]] += i
        return score.index(max(score))


class SolutionTest(unittest.TestCase):

    def test_edgeScore(self):
        self.assertEqual(Solution().edgeScore([1, 0, 0, 0, 0, 7, 7, 5]), 7)
        self.assertEqual(Solution().edgeScore([2, 0, 0, 2]), 0)

