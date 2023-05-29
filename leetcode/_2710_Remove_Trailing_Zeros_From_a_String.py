import unittest


class Solution:

    def removeTrailingZeros(self, num: str) -> str:
        n = 0
        for i in range(len(num) - 1, 0, -1):
            if num[i] == '0':
                n += 1
            else:
                break
        return num[0:len(num) - n]


class SolutionTest(unittest.TestCase):

    def test_removeTrailingZeros(self):
        self.assertEqual(Solution().removeTrailingZeros("51230100"), "512301")
        self.assertEqual(Solution().removeTrailingZeros("123"), "123")



