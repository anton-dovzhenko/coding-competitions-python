from itertools import permutations


class Solution:

    @classmethod
    def get_pandigital_products(cls):
        pp = set()
        for p in permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            n1 = int(''.join(p[0:2]))
            n2 = int(''.join(p[2:5]))
            n3 = int(''.join(p[5:9]))
            if n1 * n2 == n3:
                print(n1, n2, n3)
                pp.add(n3)

            n1 = int(''.join(p[0:1]))
            n2 = int(''.join(p[1:5]))
            n3 = int(''.join(p[5:9]))
            if n1 * n2 == n3:
                print(n1, n2, n3)
                pp.add(n3)

        return sum(pp)


