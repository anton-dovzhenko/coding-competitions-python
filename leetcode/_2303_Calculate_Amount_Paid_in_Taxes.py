import unittest
from typing import List


class Solution:

    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        last_upper = 0.
        tax = 0.
        for level in brackets:
            if income <= 0:
                break
            amount = level[0] - last_upper
            tax += min(amount, income) * level[1] * 1e-2
            income -= amount
            last_upper = level[0]
        return tax


class SolutionTest(unittest.TestCase):

    def test_calculateTax(self):
        self.assertEqual(Solution().calculateTax([[3, 50], [7, 10], [12, 25]], 10), 2.65)
        self.assertEqual(Solution().calculateTax([[1, 0], [4, 25], [5, 50]], 2), 0.25)
        self.assertEqual(Solution().calculateTax([[2, 50]], 0), 0.0)

