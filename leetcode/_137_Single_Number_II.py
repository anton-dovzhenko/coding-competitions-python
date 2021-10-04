import unittest


class Solution:

    def singleNumber(self, nums):
        result = [0] * 32
        neg = 0
        for n in nums:
            if n < 0:
                neg += 1
            n = abs(n)
            i = 0
            while n > 0:
                result[i] += n % 2
                n = n // 2
                i += 1
        missing = 0
        for i in range(len(result)):
            missing += (result[i] % 3) * 2 ** i
        return missing * (-1 if neg % 3 != 0 else 1)


class SolutionTest(unittest.TestCase):

    def test_latestDayToCross(self):
        self.assertEquals(Solution().singleNumber([2, 2, 3, 2]), 3)
        self.assertEquals(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)
        self.assertEquals(Solution().singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]), -4)


