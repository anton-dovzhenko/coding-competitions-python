class Solution:

    @classmethod
    def get_lychrel_numbers_count(cls):
        count = 0
        for n in range(1, 10_000):
            lychrel = True
            k = n
            for j in range(0, 51):
                k1 = str(k)
                k2 = k1[::-1]
                if k1 == k2 and j > 0:
                    lychrel = False
                    break
                else:
                    k = int(k1) + int(k2)
            count += lychrel
        return count


print(Solution.get_lychrel_numbers_count())

