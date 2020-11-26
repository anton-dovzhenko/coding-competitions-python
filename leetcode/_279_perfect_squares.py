import unittest


class Solution:

    def numSquares(self, n: int):
        sq = []
        i = 1
        while i ** 2 <= n:
            sq.append(i ** 2)
            i += 1

        target = {n}
        n_count = 0
        while target:
            n_count += 1
            next_target = set()
            for t in target:
                for i in sq:
                    if t == i:
                        return n_count
                    elif t - i:
                        next_target.add(t - i)
            target = next_target


class SolutionTest(unittest.TestCase):

    def test_generateMatrix(self):
        self.assertEquals(Solution().numSquares(1), 1)
        self.assertEquals(Solution().numSquares(12), 3)
        self.assertEquals(Solution().numSquares(13), 2)
        self.assertEquals(Solution().numSquares(7168), 4)


