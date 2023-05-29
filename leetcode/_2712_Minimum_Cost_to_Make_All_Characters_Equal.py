import unittest


class Solution:

    def minimumCost(self, s: str) -> int:
        cost = 0
        for i in range(1, 1 + len(s) // 2):
            if s[i - 1] != s[i]:
                cost += i

        for i in range(len(s) - 2, -1 + len(s) // 2, -1):
            if s[i + 1] != s[i]:
                cost += len(s) - i - 1

        return cost


class SolutionTest(unittest.TestCase):

    def test_minimumCost(self):
        self.assertEqual(Solution().minimumCost("0011"), 2)
        self.assertEqual(Solution().minimumCost("00111"), 2)
        self.assertEqual(Solution().minimumCost("00011"), 2)
        self.assertEqual(Solution().minimumCost("010101"), 9)


