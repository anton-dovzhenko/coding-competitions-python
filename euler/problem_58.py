class Solution:

    @classmethod
    def get_spiral_with_prime_ratio_below_10_ptc(cls):
        diagonal = 1
        square = 1
        diagonal_count = 1
        prime_count = 0

        while True:

            for i in range(4):
                diagonal += square * 2
                diagonal_count += 1
                prime_count += cls.is_prime(diagonal)
                if 10 * prime_count < diagonal_count:
                    return square * 2 + 1
            square += 1

    @classmethod
    def is_prime(cls, n):
        for i in range(2, min(1 + int(n ** 0.5), n - 1)):
            if n % i == 0:
                return False
        return True


# print(Solution.get_spiral_with_prime_ratio_below_10_ptc())


