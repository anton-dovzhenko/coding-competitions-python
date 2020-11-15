class Solution:

    @classmethod
    def get_cyclical_figurate_numbers(cls):

        polygonal = []
        for n in range(0, 6):
            polygonal.append([])

        for n in range(1, 10_000):
            p3 = int(n * (n + 1) / 2)
            p4 = int(n * n)
            p5 = int(n * (3 * n - 1) / 2)
            p6 = int(n * (2 * n - 1))
            p7 = int(n * (5 * n - 3) / 2)
            p8 = int(n * (3 * n - 2))
            if 999 < p3 < 10000:
                polygonal[0].append(p3)
            if 999 < p4 < 10000:
                polygonal[1].append(p4)
            if 999 < p5 < 10000:
                polygonal[2].append(p5)
            if 999 < p6 < 10000:
                polygonal[3].append(p6)
            if 999 < p7 < 10000:
                polygonal[4].append(p7)
            if 999 < p8 < 10000:
                polygonal[5].append(p8)

        for p in polygonal[0]:
            result = cls._is_cyclical([p], polygonal, [0])
            if result is not None:
                return sum(result)

    @classmethod
    def _is_cyclical(cls, numbers, polygonal, used_indices):
        if len(used_indices) == len(polygonal):
            if numbers[-1] % 100 == numbers[0] // 100:
                return numbers
            else:
                return None
        else:

            for i in range(len(polygonal)):
                if i in used_indices:
                    continue

                for p in polygonal[i]:
                    if numbers[-1] % 100 == p // 100:
                        r = cls._is_cyclical(numbers + [p], polygonal, used_indices + [i])
                        if r is not None:
                            return r


# print(Solution.get_cyclical_figurate_numbers())

