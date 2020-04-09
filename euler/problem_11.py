class Solution:

    def _get_max(self, number, digits):
        result = 0
        mov = 1
        mov_count = 0
        for i in range(0, len(number)):
            if number[i] == 0:
                mov = 1
                mov_count = 0
            else:
                mov *= number[i]
                if mov_count < digits - 1:
                    mov_count += 1
                else:
                    result = max(result, mov)
                    mov /= number[i - digits + 1]
        return int(result)

    def get_largest_product_in_a_grid(self, g, n):

        size = len(g)
        max_prod = 0

        for row in g:
            max_prod = max(max_prod, self._get_max(row, n))

        for j in range(0, len(g[0])):
            vertical = []
            for i in range(0, len(g)):
                vertical.append(g[i][j])
            max_prod = max(max_prod, self._get_max(vertical, n))

        for i in range(0, len(g) - n):
            diagonal = []
            for j in range(0, len(g) - i):
                diagonal.append(g[i + j][j])
            max_prod = max(max_prod, self._get_max(diagonal, n))

        for j in range(1, len(g[0]) - n):
            diagonal = []
            for i in range(0, len(g) - j):
                diagonal.append(g[i][j + i])
            max_prod = max(max_prod, self._get_max(diagonal, n))

        for k in range(0, size):
            diagonal = []
            i = k
            j = size - 1
            while i < size and j > -1:
                diagonal.append(g[i][j])
                i += 1
                j += -1
            max_prod = max(max_prod, self._get_max(diagonal, n))

        for k in range(0, size):
            diagonal = []
            i = 0
            j = k
            while i < size and j > -1:
                diagonal.append(g[i][j])
                i += 1
                j -= 1
            max_prod = max(max_prod, self._get_max(diagonal, n))

        return max_prod

