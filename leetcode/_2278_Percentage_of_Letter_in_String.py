import unittest


class Solution:

    def percentageLetter(self, s: str, letter: str) -> int:
        return int(100 * s.count(letter) / len(s))


class SolutionTest(unittest.TestCase):

    def test_latestDayToCross(self):
        self.assertEquals(Solution().percentageLetter("foobar", "o"), 33)
        self.assertEquals(Solution().percentageLetter("jjjj", "k"), 0)
