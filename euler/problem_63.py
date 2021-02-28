class Solution:

    @classmethod
    def solve(cls):
        c = 0
        for i in range(1, 100):
            for p in range(1, 100):
                v = i ** p
                if len(str(v)) == p:
                    c += 1
                #     print("%s ** %s = %s" % (i, p, v))
        return c

