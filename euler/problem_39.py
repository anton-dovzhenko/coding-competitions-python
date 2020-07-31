class Solution:

    @classmethod
    def get_max_solutions(cls, max_p):
        s = {}

        for a in range(1, max_p):
            for b in range(a, max_p):
                c = (a ** 2 + b ** 2) ** 0.5
                if (a + b + c) <= max_p:
                    if c.is_integer():
                        p = a + b + int(c)
                        s[p] = s.get(p, 0) + 1
                else:
                    break

        m = 0
        v = None
        for entry in s.items():
            if entry[1] > m:
                m = entry[1]
                v = entry[0]
        return v

