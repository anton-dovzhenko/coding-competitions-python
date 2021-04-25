class Solution:

    def sumBase(self, n, k):
        s = 0
        while n > 0:
            s += n % k
            n = n // k
        return s


print(Solution().sumBase(34, 6))
print(Solution().sumBase(10, 10))

