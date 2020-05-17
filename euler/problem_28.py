class Solution:

    @classmethod
    def get_number_spiral_diagonals(cls, n):
        d = 1
        s = 1

        for i in range(1, int(1 + (n - 1) / 2)):
            size = 2 * i
            s += 4 * d + 10 * size
            d += 4 * size

        return s

