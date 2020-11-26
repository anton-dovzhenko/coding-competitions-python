import unittest


class Solution:

    def partition(self, s):
        L = len(s)
        d = {}

        for i in range(0, L):
            for j in range(i, L):
                if self._is_palindrome(s, i, j):
                    if i not in d:
                        d[i] = []
                    d[i].append(j + 1)

        partitions = []
        self._get_partitions(d, [0], partitions)
        p = []
        for part in partitions:
            next_part = []
            for i in range(0, len(part) - 1):
                next_part.append(s[part[i]:part[i + 1]])
            p.append(next_part)
        return p

    def _is_palindrome(self, s, st, end):
        while st < end:
            if s[st] != s[end]:
                return False
            end -= 1
            st += 1
        return True

    def _get_partitions(self, d, p, partitions):
        if p[-1] == len(d):
            partitions.append(p)
        if p[-1] not in d:
            return
        for i in d[p[-1]]:
            self._get_partitions(d, p + [i], partitions)


class SolutionTest(unittest.TestCase):

    def test_generateMatrix(self):
        self.assertEquals(Solution().partition("aab"), [['a', 'a', 'b'], ['aa', 'b']])


