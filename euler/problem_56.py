class Solution:

    @classmethod
    def get_powerful_digit_sum(cls, A, B):

        result = 0
        for a in range(1, A):
            for b in range(1, B):
                n = a ** b
                s = 0
                while n > 0:
                    s += n % 10
                    n //= 10
                result = max(result, s)

        return result

