class Solution:

    def get_maximum_path_sum_i(self, path):
        path = self._parse(path)
        for i in range(1, len(path)):
            for j in range(0, len(path[i])):
                e1 = path[i - 1][max(0, j - 1)]
                e2 = path[i - 1][min(j, i - 1)]
                path[i][j] += max(e1, e2)
        return max(path[-1])

    def _parse(self, path):
        path = path.split("\n")
        path = [list(map(int, x.split())) for x in path]
        return path

