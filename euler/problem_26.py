class Solution:

    def get_max_recurring_cycle(self, n):
        max_d = 0
        max_i = 0
        for i in range(2, n):
            for j in range(1, 2 * n):
                if (10 ** j - 1) % i == 0:
                    if j > max_d:
                        max_d = j
                        max_i = i
                    break
        return max_i

