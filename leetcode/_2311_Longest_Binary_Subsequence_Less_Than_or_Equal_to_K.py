import unittest


class Solution:

    def longestSubsequence(self, s: str, k: int) -> int:
        s = (int(x) for x in reversed(s))
        length = 0
        num = 0
        for n in s:
            next_num = num + 2 ** length
            if n == 0:
                length += 1
            elif next_num <= k:
                num = next_num
                length += 1
        return length


class SolutionTest(unittest.TestCase):

    def test_longestSubsequence(self):
        self.assertEqual(Solution().longestSubsequence("1001010", 5), 5)
        self.assertEqual(Solution().longestSubsequence("00101001", 1), 6)


