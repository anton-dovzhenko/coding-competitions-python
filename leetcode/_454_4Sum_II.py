import collections


class Solution:

    def fourSumCount(self, A, B, C, D):
        ab = collections.Counter(a + b for a in A for b in B)
        return sum(ab[-c - d] for c in C for d in D)


# print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
# print(Solution().fourSumCount([0, 1, -1],
#                               [-1, 1, 0],
#                               [0, 0, 1],
#                               [-1, 1, 1]))

