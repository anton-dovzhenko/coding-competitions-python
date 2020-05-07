class Solution:

    def get_n_digit_fibonacci_number(self, n):
        f1 = 1
        f2 = 1
        i = 2
        while len(str(f2)) < n:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            i += 1

        return i

