import unittest
import numpy as np


class Solution:

    def greatestLetter(self, s: str) -> str:
        lower = np.zeros(26)
        upper = np.zeros(26)
        a = ord('a')
        A = ord('A')
        for c in s:
            c = ord(c)
            if c >= a:
                lower[c - a] += 1
            else:
                upper[c - A] += 1
        counts = np.flatnonzero(upper * lower)
        return '' if 0 == len(counts) else chr(counts[-1] + A)


class SolutionTest(unittest.TestCase):

    def test_greatestLetter(self):
        self.assertEqual(Solution().greatestLetter("lEeTcOdE"), "E")
        self.assertEqual(Solution().greatestLetter("arRAzFif"), "R")
        self.assertEqual(Solution().greatestLetter("AbCdEfGhIjK"), "")

