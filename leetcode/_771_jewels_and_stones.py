import unittest


class Solution:

    def numJewelsInStones(self, J, S):
        j_count = 0
        for j in J:
            j_count += S.count(j)
        return j_count


class SolutionTest(unittest.TestCase):

    def test_numJewelsInStones(self):
        self.assertEquals(Solution().numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEquals(Solution().numJewelsInStones("z", "ZZ"), 0)


