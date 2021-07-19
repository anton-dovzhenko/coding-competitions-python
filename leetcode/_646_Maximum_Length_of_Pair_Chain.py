import math


class Solution:

    def findLongestChain(self, pairs):
        pairs = sorted(pairs, key=lambda x: x[1])
        length = 0
        prev = -math.inf
        for p in pairs:
            if p[0] > prev:
                length += 1
                prev = p[1]
        return length


# print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))
# print(Solution().findLongestChain([[1, 2], [7, 8], [4, 5]]))
