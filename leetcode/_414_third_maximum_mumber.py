class Solution:

    def thirdMax(self, nums):
        s = sorted(set(nums))
        return s[-3 if len(s) >= 3 else -1]


# print(Solution().thirdMax([1, 2]))
# print(Solution().thirdMax([2, 2, 3, 1]))
