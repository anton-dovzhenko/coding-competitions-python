import unittest


class Solution:

    def generateMatrix(self, n):
        m = []
        for i in range(0, n):
            m.append(n * [0])
        d = 0  # 0 - right, 1 - down, 2 - left, 3 - up
        i = 1
        p = [0, -1]
        while i < n * n + 1:
            d = d % 4
            if d == 0:
                if p[1] < n - 1 and m[p[0]][p[1] + 1] == 0:
                    p[1] += 1
                    m[p[0]][p[1]] = i
                    i += 1
                else:
                    d += 1
            elif d == 1:
                if p[0] < n - 1 and m[p[0] + 1][p[1]] == 0:
                    p[0] += 1
                    m[p[0]][p[1]] = i
                    i += 1
                else:
                    d += 1
            elif d == 2:
                if p[1] > 0 and m[p[0]][p[1] - 1] == 0:
                    p[1] -= 1
                    m[p[0]][p[1]] = i
                    i += 1
                else:
                    d += 1
            elif d == 3:
                if p[0] > 0 and m[p[0] - 1][p[1]] == 0:
                    p[0] -= 1
                    m[p[0]][p[1]] = i
                    i += 1
                else:
                    d += 1
            else:
                raise ValueError()

        return m


class SolutionTest(unittest.TestCase):

    def test_generateMatrix(self):
        self.assertEquals(Solution().generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        self.assertEquals(Solution().generateMatrix(4), [[1, 2, 3, 4],
                                                         [12, 13, 14, 5],
                                                         [11, 16, 15, 6],
                                                         [10, 9, 8, 7]])
        self.assertEquals(Solution().generateMatrix(5), [[1, 2, 3, 4, 5],
                                                         [16, 17, 18, 19, 6],
                                                         [15, 24, 25, 20, 7],
                                                         [14, 23, 22, 21, 8],
                                                         [13, 12, 11, 10, 9]])


