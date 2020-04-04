class Solution:

    def get_fibonacci_even_sum(self, limit):
        n1 = 1
        n2 = 2
        s = n2

        while n1 + n2 < limit:
            n = n1 + n2
            n1 = n2
            n2 = n
            if n % 2 == 0:
                s += n

        return s

