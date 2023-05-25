import unittest


class Solution:

    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s) // 2):
            j = len(s) - 1 - i
            c = chr(min(ord(s[i]), ord(s[j])))
            s[i] = s[j] = c
        return ''.join(s)


class SolutionTest(unittest.TestCase):

    def test_makeSmallestPalindrome(self):
        self.assertEqual(Solution().makeSmallestPalindrome("egcfe"), "efcfe")
        self.assertEqual(Solution().makeSmallestPalindrome("abcd"), "abba")
        self.assertEqual(Solution().makeSmallestPalindrome("seven"), "neven")



