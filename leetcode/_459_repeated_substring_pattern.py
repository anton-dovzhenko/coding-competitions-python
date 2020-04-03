import unittest


class Solution:

    def repeatedSubstringPattern(self, s):
        s_len = len(s)
        if s_len < 2:
            return False
        for i in range(2, s_len + 1):
            if s_len % i == 0:
                sub_len = int(s_len / i)
                if s[:sub_len] * i == s:
                    return True
        return False


class SolutionTest(unittest.TestCase):

    def test_repeatedSubstringPattern(self):
        self.assertTrue(Solution().repeatedSubstringPattern("abab"))
        self.assertFalse(Solution().repeatedSubstringPattern("aba"))
        self.assertTrue(Solution().repeatedSubstringPattern("abcabcabcabc"))
        self.assertTrue(Solution().repeatedSubstringPattern("bb"))
        self.assertTrue(Solution().repeatedSubstringPattern("ababab"))
        self.assertTrue(Solution().repeatedSubstringPattern("ababababab"))


