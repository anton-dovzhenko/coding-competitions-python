class Solution:

    @classmethod
    def get_distinct_powers(cls, a, b):
        d = set()
        for i in range(2, a + 1):
            for j in range(2, b + 1):
                d.add(i ** j)

        return len(d)


