class Solution:

    @classmethod
    def get_coin_sums(cls, coins, target, start=0):
        count = 0
        for i in range(start, len(coins)):
            c = coins[i]
            if c < target:
                count += cls.get_coin_sums(coins, target - c, i)
            elif c == target:
                count += 1
                break
            else:
                break
        return count

