class Solution:

    @classmethod
    def get_cubic_permutations(cls, N):

        d = {}
        min_n = 1_000_000
        n = 1
        while n < 100_000:
            cube = n ** 3
            key = ''.join(sorted(str(cube)))
            if key not in d:
                d[key] = [n]
            else:
                d[key].append(n)
                if len(d[key]) == N:
                    min_n = min(min_n, d[key][0])
            n += 1
        return min_n ** 3
