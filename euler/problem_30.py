class Solution:

    @classmethod
    def get_digit_fifth_powers(cls, p):
        total = 0
        for i in range(2, 10000000):
            s = 0
            n = i
            while n > 0:
                s += (n % 10) ** p
                n = n // 10
            if s == i:
                total += s
        return total

