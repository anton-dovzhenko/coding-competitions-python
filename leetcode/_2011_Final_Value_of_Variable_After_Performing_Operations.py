import unittest


class Solution:

    def finalValueAfterOperations(self, operations):
        x = 0
        for o in operations:
            if o in ("X++", "++X"):
                x += 1
            elif o in ("X--", "--X"):
                x -= 1
            else:
                raise Exception("Incorrect operation %s" % o)

        return x


class SolutionTest(unittest.TestCase):

    def test_finalValueAfterOperations(self):
        self.assertEquals(Solution().finalValueAfterOperations(["--X", "X++", "X++"]), 1)
        self.assertEquals(Solution().finalValueAfterOperations(["++X","++X","X++"]), 3)
        self.assertEquals(Solution().finalValueAfterOperations(["X++","++X","--X","X--"]), 0)


