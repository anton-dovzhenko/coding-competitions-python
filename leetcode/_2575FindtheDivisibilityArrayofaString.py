import unittest
from typing import List


class Solution:

    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        answer = [0] * n
        number = 0
        for i in range(0, n):
            number = (number * 10 + ord(word[i]) - ord('0')) % m
            if number == 0:
                answer[i] = 1
        return answer


class SolutionTest(unittest.TestCase):

    def test_divisibilityArray(self):
        self.assertEqual(Solution().divisibilityArray("998244353",  3), [1, 1, 0, 0, 0, 1, 1, 0, 0])
        self.assertEqual(Solution().divisibilityArray("1010",  10), [0, 1, 0, 1])





