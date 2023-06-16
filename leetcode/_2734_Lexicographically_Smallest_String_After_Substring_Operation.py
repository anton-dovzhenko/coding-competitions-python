import unittest


class Solution:

    def smallestString(self, s: str) -> str:
        s = list(s)
        not_a_cnt = 0
        for i in range(len(s)):
            if s[i] == 'a':
                if not_a_cnt > 0:
                    break
            else:
                s[i] = chr(ord(s[i]) - 1)
                not_a_cnt += 1

        if len(s) > 0 and not_a_cnt == 0:
            s[-1] = 'z'
        return ''.join(s)


class SolutionTest(unittest.TestCase):

    def test_smallestString(self):
        self.assertEqual(Solution().smallestString("cbabc"), "baabc")
        self.assertEqual(Solution().smallestString("acbbc"), "abaab")
        self.assertEqual(Solution().smallestString("leetcode"), "kddsbncd")
        self.assertEqual(Solution().smallestString("cbabc"), "baabc")
        self.assertEqual(Solution().smallestString("a"), "z")
        self.assertEqual(Solution().smallestString("aa"), "az")


