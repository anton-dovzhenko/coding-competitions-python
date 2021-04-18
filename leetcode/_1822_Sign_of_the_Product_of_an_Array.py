from functools import reduce
from operator import mul


class Solution:

    def arraySign(self, nums):
        return reduce(mul, ((n > 0) - (n < 0) for n in nums))


print(Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(Solution().arraySign([1, 5, 0, 2, -3]))
print(Solution().arraySign([-1, 1, -1, 1, -1]))
