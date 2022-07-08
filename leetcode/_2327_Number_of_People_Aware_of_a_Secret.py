class Solution:

    MOD = 10 ** 9 + 7

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        d = {0: 1}
        for i in range(1, n):
            next_d = {0: 0}
            for key, value in d.items():
                if forget > key + 1 >= delay:
                    next_d[0] = next_d[0] + value
                if key + 1 < forget:
                    next_d[key + 1] = value
            d = next_d
        return sum(d.values()) % self.MOD


print(Solution().peopleAwareOfSecret(6, 2, 4))
print(Solution().peopleAwareOfSecret(4, 1, 3))
print(Solution().peopleAwareOfSecret(684, 18, 496))