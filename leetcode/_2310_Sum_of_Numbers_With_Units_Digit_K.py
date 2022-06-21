import unittest


class Solution:

    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10 == 0 else -1
        N = num
        min_size = num
        while num > 0:
            if num % k == 0:
                min_size = min(min_size, num // k)
            num -= 10
        return -1 if k != 1 and N == min_size else min_size


class SolutionTest(unittest.TestCase):

    def test_minimumNumbers(self):
        self.assertEqual(Solution().minimumNumbers(58, 9), 2)
        self.assertEqual(Solution().minimumNumbers(37, 2), -1)
        self.assertEqual(Solution().minimumNumbers(0, 7), 0)
        self.assertEqual(Solution().minimumNumbers(1, 1), 1)
        self.assertEqual(Solution().minimumNumbers(5, 1), 5)
        self.assertEqual(Solution().minimumNumbers(4, 0), -1)
        self.assertEqual(Solution().minimumNumbers(40, 0), 1)
        self.assertEqual(Solution().minimumNumbers(20, 1), 10)

