import unittest
from typing import List


class Solution:

    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer: List[int] = [0] * n
        for i in reversed(range(0, n - 1)):
            answer[i] = nums[i + 1] + answer[i + 1]
        left_sum = 0
        for i in range(1, n):
            left_sum += nums[i - 1]
            answer[i] = abs(answer[i] - left_sum)
        return answer


class SolutionTest(unittest.TestCase):

    def test_leftRigthDifference(self):
        self.assertEqual(Solution().leftRigthDifference([10, 4, 8, 3]), [15, 1, 11, 22])
        self.assertEqual(Solution().leftRigthDifference([1]), [0])

