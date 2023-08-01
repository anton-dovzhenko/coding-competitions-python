import itertools
import unittest


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        words = [a, b, c]
        results = []
        for p in itertools.permutations([0, 1, 2]):
            results.append(self._append(self._append(words[p[0]], words[p[1]]), words[p[2]]))
        min_len = min(len(x) for x in results)
        return sorted(filter(lambda x: len(x) == min_len, results))[0]

    def _append(self, x, y):
        if x in y:
            return y
        if y in x:
            return x
        n = min(len(x), len(y))
        matched = 0
        for i in range(n):
            if x[len(x) - 1 - i:] == y[:i + 1]:
                matched = i + 1
        return x + y[matched:]


class SolutionTest(unittest.TestCase):

    def test_minimumString(self):
        self.assertEqual(Solution().minimumString("abc", "bca", "aaa"), "aaabca")
        self.assertEqual(Solution().minimumString("ab", "ba", "aba"), "aba")
        self.assertEqual(Solution().minimumString("cab", "a", "b"), "cab")


