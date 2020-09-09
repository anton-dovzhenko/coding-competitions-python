class Solution:

    @classmethod
    def get_count_greater_than_mil(cls):
        count = 0
        for n in range(1, 101):
            for r in range(1, n):
                f = 1
                for i in range(1, r + 1):
                    f *= (n - r + i) / i
                count += f >= 1000000

        return count


# print(Solution.get_count_greater_than_mil())

