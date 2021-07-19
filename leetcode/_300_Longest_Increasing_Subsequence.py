class Solution:

    # not efficient, but simple
    def lengthOfLIS(self, nums):
        n = len(nums)
        cnt = [1] * n
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    cnt[j] = max(cnt[j], cnt[i] + 1)
        return max(cnt)


print(4 == Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(4 == Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(1 == Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))


