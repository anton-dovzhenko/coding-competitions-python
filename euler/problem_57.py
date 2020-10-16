class Solution:

    @classmethod
    def get_specific_square_root_convergents(cls, n):
        n = 1
        d = 2
        cnt = 0
        print(1 + n / d)
        for i in range(0, 1000):
            d_temp = 2 * d + n
            n = d
            d = d_temp
            if len(str(n + d)) > len(str(d)):
                cnt += 1

        return cnt


