class Solution:

    def get_sum_square_difference(self, n):
        # sum of squares is     n*(n+1)*(2*n+1)/6
        # sum of cubes is       (n*(n+1)/2) ** 2
        return int(n * (n + 1) / 2 * (n * (n + 1) / 2 - (2 * n + 1) / 3))


