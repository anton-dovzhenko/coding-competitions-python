import unittest
import math


class Solution:

    def minMutation(self, start, end, bank) -> int:
        d = {}
        for w in bank:
            for i in range(0, len(w)):
                key = w[:i] + '.' + w[i + 1:]
                if key not in d:
                    d[key] = []
                d[key].append(w)
        length = self._get_min_genetic_mutation([start], end, d)
        return -1 if math.isinf(length) else length

    def _get_min_genetic_mutation(self, starts, end, bankd) -> int:
        if end in starts:
            return 0
        if len(starts) == 0 or len(bankd) == 0:
            return float('inf')
        next_begin_words = []
        for bw in starts:
            for i in range(0, len(bw)):
                key = bw[:i] + '.' + bw[i + 1:]
                if key in bankd:
                    next_begin_words = next_begin_words + bankd[key]
                    del bankd[key]

        return 1 + self._get_min_genetic_mutation(next_begin_words, end, bankd)


class SolutionTest(unittest.TestCase):

    def test_ladderLength1(self):
        self.assertEquals(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1)
        self.assertEquals(Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2)
        self.assertEquals(Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]), 3)
