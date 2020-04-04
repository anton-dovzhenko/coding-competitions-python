class Solution:

    def get_largest_prime_factor(self, n):
        m_factor = 1
        f = 2
        while n > 1:
            if n % f == 0:
                m_factor = f
                n /= f
            else:
                f += 1
        return m_factor

