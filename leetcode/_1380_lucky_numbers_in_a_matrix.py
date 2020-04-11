import unittest


class Solution:

    def luckyNumbers(self, matrix):

        lucky = []
        mmin = set()
        for row in matrix:
            mmin.add(min(row))
        for j in range(0, len(matrix[0])):
            mm = -1
            for i in range(0, len(matrix)):
                mm = max(mm, matrix[i][j])
            if mm in mmin:
                lucky.append(mm)

        return lucky


class SolutionTest(unittest.TestCase):

    def test_maxValueAfterReverse(self):
        self.assertEquals(Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]), [15])
        self.assertEquals(Solution().luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]), [12])
        self.assertEquals(Solution().luckyNumbers([[7, 8], [1, 2]]), [7])


