from typing import List


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = 0 if matrix[i][j] == "0" else 1

        for i in range(len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i][j - 1]

        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                n = matrix[i][j]
                if i > 0 and n <= matrix[i - 1][j]:
                    continue
                length = n
                area = max(area, n)
                for k in range(i + 1, len(matrix)):
                    length = min(length, matrix[k][j])
                    if length == 0:
                        break
                    area = max(area, length * (k + 1 - i))

        return area
