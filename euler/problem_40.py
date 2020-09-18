class Solution:

    @classmethod
    def get_champernownes_constant(cls):
        d = "0123456789"
        c = 1
        while len(d) < 1_000_0001:
            for i in range(0, 10):
                d += str(c) + str(i)
            c += 1

        return int(d[1]) * int(d[10]) * int(d[100]) * int(d[1_000]) * int(d[10_000]) * int(d[100_000]) * \
               int(d[1_000_000])
