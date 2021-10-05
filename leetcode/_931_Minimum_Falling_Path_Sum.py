import unittest


class Solution:

    def minFallingPathSum(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += min(
                    matrix[i - 1][j],
                    matrix[i - 1][max(0, j - 1)],
                    matrix[i - 1][min(len(matrix[i]) - 1, j + 1)])
        return min(matrix[-1])


class SolutionTest(unittest.TestCase):

    def test_minFallingPathSum(self):
        self.assertEquals(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]), 13)
        self.assertEquals(Solution().minFallingPathSum([[-19, 57], [-40, -5]]), -59)
        self.assertEquals(Solution().minFallingPathSum([[-48]]), -48)


