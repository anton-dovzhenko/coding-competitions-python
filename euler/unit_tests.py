import unittest

from euler import problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8, problem_9, \
    problem_10


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

    def test_problem7(self):
        self.assertEquals(problem_7.Solution().get_prime(1), 2)
        self.assertEquals(problem_7.Solution().get_prime(2), 3)
        self.assertEquals(problem_7.Solution().get_prime(3), 5)
        self.assertEquals(problem_7.Solution().get_prime(4), 7)
        self.assertEquals(problem_7.Solution().get_prime(5), 11)
        self.assertEquals(problem_7.Solution().get_prime(6), 13)

    def test_problem8(self):
        self.assertEquals(problem_8.Solution().get_largest_product_in_a_series(
            """73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450""",
            4), 5832)

    def test_problem9(self):
        self.assertEquals(problem_9.Solution().get_special_pythagorean_triplet(12), 60)
        self.assertEquals(problem_9.Solution().get_special_pythagorean_triplet(1000), 31875000)

    def test_problem10(self):
        self.assertEquals(problem_10.Solution().get_sum_of_primes(10), 17)
        self.assertEquals(problem_10.Solution().get_sum_of_primes(2_000_000), 142913828922)

