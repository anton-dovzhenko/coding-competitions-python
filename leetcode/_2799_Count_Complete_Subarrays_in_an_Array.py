import unittest
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        unique = dict.fromkeys(set(nums), 0)
        unique_nums = 0
        start = 0
        end = 0
        while end < len(nums):

            if unique[nums[end]] == 0:
                unique_nums += 1
            unique[nums[end]] += 1

            if unique_nums == len(unique):
                cnt += len(nums) - end
                unique[nums[start]] -= 1
                if unique[nums[start]] == 0:
                    unique_nums -= 1
                start += 1

                unique[nums[end]] -= 1
                if unique[nums[end]] == 0:
                    unique_nums -= 1
            else:
                end += 1
        return cnt


class SolutionTest(unittest.TestCase):

    def test_numberOfEmployeesWhoMetTarget(self):
        self.assertEqual(Solution().countCompleteSubarrays([1, 3, 1, 2, 2]), 4)
        self.assertEqual(Solution().countCompleteSubarrays([5, 5, 5, 5]), 10)
        self.assertEqual(Solution().countCompleteSubarrays([1454, 1789, 1454]), 3)
        self.assertEqual(Solution().countCompleteSubarrays([381, 1304, 381, 758, 1304, 381, 758]), 14)
