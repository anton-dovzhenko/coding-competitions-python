class Solution:

    @classmethod
    def get_greatest_pandigital(cls):
        greatest = '0'
        for i in range(1, 10000):
            n = str(i)
            for j in range(2, 10):
                if cls.is_pandigital(n):
                    greatest = max(greatest, n)
                    break
                elif len(n) >= 9:
                    break
                else:
                    n += str(i * j)

        return int(greatest)

    @classmethod
    def is_pandigital(cls, n):
        if len(n) != 9:
            return False
        c = 9 * [0]
        for i in n:
            if i == '0':
                return False
            c[ord(i) - ord('1')] += 1
            if c[ord(i) - ord('1')] > 1:
                return False
        return True

