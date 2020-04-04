import unittest

from euler import problem_1, problem_2, problem_3, problem_4, problem_5, problem_6


class EulerTest(unittest.TestCase):

    def test_problem1(self):
        self.assertEquals(problem_1.Solution().get_multiples_of_3_and_5(10), 23)
        self.assertEquals(problem_1.Solution().get_multiples_of_3_and_5(1000), 233168)

    def test_problem2(self):
        self.assertEquals(problem_2.Solution().get_fibonacci_even_sum(100), 44)
        self.assertEquals(problem_2.Solution().get_fibonacci_even_sum(4_000_000), 4613732)

    def test_problem3(self):
        self.assertEquals(problem_3.Solution().get_largest_prime_factor(13195), 29)
        self.assertEquals(problem_3.Solution().get_largest_prime_factor(600851475143), 6857)

    def test_problem4(self):
        self.assertEquals(problem_4.Solution().get_largest_palindrome_product(2), 9009)
        self.assertEquals(problem_4.Solution().get_largest_palindrome_product(3), 906609)

    def test_problem5(self):
        self.assertEquals(problem_5.Solution().smallest_multiple(10), 2520)
        self.assertEquals(problem_5.Solution().smallest_multiple(20), 232792560)

    def test_problem6(self):
        self.assertEquals(problem_6.Solution().get_sum_square_difference(10), 2640)
        self.assertEquals(problem_6.Solution().get_sum_square_difference(100), 25164150)

