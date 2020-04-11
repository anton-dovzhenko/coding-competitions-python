import unittest
import numpy as np


class Solution:

    def maxValueAfterReverse(self, nums):
        nums = np.asarray(nums)
        max_gain = 0
        i_gain = 0
        j_gain = 0
        l = len(nums)
        for i in range(0, l):
            for j in range(i + 1, l):
                val0 = (abs(nums[i] - nums[i - 1]) if i > 0 else 0) \
                       + abs(nums[j] - nums[j + 1]) if j < l - 1 else 0
                val1 = (abs(nums[j] - nums[i - 1]) if i > 0 else 0) \
                       + abs(nums[i] - nums[j + 1]) if j < l - 1 else 0

                if val1 - val0 > max_gain:
                    max_gain = val1 - val0
                    i_gain = i
                    j_gain = j
        nums[i_gain:j_gain + 1] = nums[i_gain:j_gain + 1][::-1]
        arr_val = 0
        for i in range(0, l - 1):
            arr_val += abs(nums[i + 1] - nums[i])
        return arr_val


class SolutionTest(unittest.TestCase):

    def test_maxValueAfterReverse(self):
        self.assertEquals(Solution().maxValueAfterReverse([2, 3, 1, 5, 4]), 10)
        self.assertEquals(Solution().maxValueAfterReverse([2, 4, 9, 24, 2, 1, 10]), 68)

