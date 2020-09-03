from euler import utils


class Solution:

    @classmethod
    def get_self_powers(cls, limit):
        n = 0
        mod = int(1e11)
        for i in range(1, limit + 1):
            n += (i ** i) % mod
            n = n % mod
        return str(n)[-10:]

