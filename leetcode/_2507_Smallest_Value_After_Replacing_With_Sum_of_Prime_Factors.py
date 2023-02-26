import unittest


class Solution:

    def smallestValue(self, n: int) -> int:
        last_n = n
        while True:
            next_n = 0
            cnt = 0
            div = 2
            while div <= n:
                if n % div == 0:
                    next_n += div
                    cnt += 1
                    n //= div
                else:
                    div += 1
            if cnt == 1 or next_n == last_n:
                return next_n
            else:
                last_n = n = next_n


class SolutionTest(unittest.TestCase):

    def test_longestSquareStreak(self):
        self.assertTrue(Solution().smallestValue(15), 15)
        self.assertTrue(Solution().smallestValue(4), 4)


