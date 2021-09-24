import unittest


class Solution:

    def sumOfBeauties(self, nums):
        num_max = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            num_max[i] = (max(num_max[i - 1], nums[i]))

        s = 0
        min_tail = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if num_max[i - 1] < nums[i] < min_tail:
                s += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                s += 1
            min_tail = min(min_tail, nums[i])

        return s


class SolutionTest(unittest.TestCase):

    def test_sumOfBeauties(self):
        self.assertEquals(Solution().sumOfBeauties([1, 2, 3]), 2)
        self.assertEquals(Solution().sumOfBeauties([2, 4, 6, 4]), 1)
        self.assertEquals(Solution().sumOfBeauties([3, 2, 1]), 0)
        self.assertEquals(Solution().sumOfBeauties([6, 7, 7, 9, 3, 9, 3, 4, 4, 1]), 0)
