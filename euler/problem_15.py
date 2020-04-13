class Solution:

    def get_lattice_paths(self, n):
        lengths = [1] * (n + 1)
        for i in range(0, n):
            for j in range(1, n + 1):
                lengths[j] += lengths[j - 1]
        return lengths[-1]

