class Solution:

    def largestPerimeter(self, nums):
        nums = sorted(nums, reverse=True)
        for i in range(0, len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0


print(Solution().largestPerimeter([1, 2, 1]) == 0)
print(Solution().largestPerimeter([3, 2, 3, 4]) == 10)
print(Solution().largestPerimeter([3, 6, 2, 3]) == 8)


