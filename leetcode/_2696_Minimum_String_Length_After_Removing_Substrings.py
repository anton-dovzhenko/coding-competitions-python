import unittest


class Solution:

    def minLength(self, s: str) -> int:
        n = len(s)
        while True:
            s = s.replace('AB', '')
            s = s.replace('CD', '')
            if n == len(s):
                break
            else:
                n = len(s)
        return n


class SolutionTest(unittest.TestCase):

    def test_minLength(self):
        self.assertEqual(Solution().minLength("ABFCACDB"), 2)
        self.assertEqual(Solution().minLength("ACBBD"), 5)


