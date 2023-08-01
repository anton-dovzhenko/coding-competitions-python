import unittest
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(x >= target for x in hours)

class SolutionTest(unittest.TestCase):

    def test_numberOfEmployeesWhoMetTarget(self):
        self.assertEqual(Solution().numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2), 3)
        self.assertEqual(Solution().numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6), 0)




