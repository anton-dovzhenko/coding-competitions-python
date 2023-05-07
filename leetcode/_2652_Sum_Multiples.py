import unittest


class Solution:

    def sumOfMultiples(self, n: int) -> int:
        return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0 or x % 7 == 0, range(1, n + 1)))


class SolutionTest(unittest.TestCase):

    def test_sumOfMultiples(self):
        self.assertEqual(Solution().sumOfMultiples(7), 21)
        self.assertEqual(Solution().sumOfMultiples(9), 30)
        self.assertEqual(Solution().sumOfMultiples(10), 40)



