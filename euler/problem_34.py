class Solution:

    @classmethod
    def get_digit_factorials(cls):
        fsum = 0
        f = [1, 1]
        for i in range(2, 10):
            f.append(f[-1] * i)
        for n in range(3, 9999999):
            if n == cls.get_factorial_sum(f, n):
                print(n)
                fsum += n

        return fsum

    @classmethod
    def get_factorial_sum(cls, f, n):
        s = 0
        while n > 0:
            s += f[n % 10]
            n = n // 10
        return s


