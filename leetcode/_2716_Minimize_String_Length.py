import unittest


class Solution:

    def minimizedStringLength(self, s: str) -> int:
        letters = [False] * 28
        for c in s:
            letters[ord(c) - ord('a')] = True
        return sum(letters)


class SolutionTest(unittest.TestCase):

    def test_minimizedStringLength(self):
        self.assertEqual(Solution().minimizedStringLength("aaabc"), 3)
        self.assertEqual(Solution().minimizedStringLength("cbbd"), 3)
        self.assertEqual(Solution().minimizedStringLength("dddaaa"), 2)


