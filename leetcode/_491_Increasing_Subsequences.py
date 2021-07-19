class Solution:

    def findSubsequences(self, nums):
        s = []
        sequence = []
        self.fs(nums, 0, s, sequence)
        return s

    def fs(self, nums, start, s, sequence):
        if len(sequence) > 1:
            s.append(sequence)
        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue
            ns = []
            if len(sequence) == 0:
                ns = [nums[i]]
            elif nums[i] >= sequence[-1]:
                ns = sequence.copy()
                ns.append(nums[i])
            if len(ns) > 0:
                used.add(nums[i])
                self.fs(nums, i + 1, s, ns)


# print(Solution().findSubsequences([4, 6, 7, 7]))
# print(Solution().findSubsequences([4, 4, 3, 2, 1]))

