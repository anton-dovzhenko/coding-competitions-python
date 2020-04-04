class Solution:

    def get_multiples_of_3_and_5(self, n):
        s = 0
        for i in range(1, n):
            if i % 3 == 0 or i % 5 == 0:
                s += i
        return s

