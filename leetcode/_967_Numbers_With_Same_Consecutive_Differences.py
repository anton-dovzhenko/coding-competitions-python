import unittest
from typing import List


class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        numbers: List[int] = []
        self.nextNum(n, k, 0, numbers)
        return numbers

    def nextNum(self, n: int, k: int, number: int, numbers: List[int]):
        if n == 0:
            numbers.append(number)
        else:
            for i in range(10):
                if number == 0:
                    if i > 0:
                        self.nextNum(n - 1, k, i, numbers)
                else:
                    digit = number % 10
                    if abs(i - digit) == k:
                        self.nextNum(n - 1, k, number * 10 + i, numbers)


class SolutionTest(unittest.TestCase):

    def test_numsSameConsecDiff(self):
        self.assertEquals(Solution().numsSameConsecDiff(3, 7), [181, 292, 707, 818, 929])
        self.assertEquals(Solution().numsSameConsecDiff(2, 1), [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98])
