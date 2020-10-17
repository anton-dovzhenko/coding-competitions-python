import unittest

from euler import utils, problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8, \
    problem_9, \
    problem_10, problem_12, problem_13, problem_11, problem_14, problem_15, problem_16, problem_17, problem_18, \
    problem_19, problem_20, problem_21, problem_22, problem_23, problem_24, problem_25, problem_26, problem_27, \
    problem_28, problem_29, problem_30, problem_31, problem_32, problem_33, problem_35, problem_36, problem_37, \
    problem_38, problem_39, problem_41, problem_42, problem_44, problem_45, problem_47, problem_48, problem_49, \
    problem_58, problem_53, problem_55, problem_34, problem_40, problem_43, problem_57, problem_46


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

    def test_problem11(self):
        self.assertEquals(problem_11.Solution().get_largest_product_in_a_grid([
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]], 4), 70600674)

    def test_problem12(self):
        self.assertEquals(problem_12.Solution().get_highly_divisible_triangular_number(5), 28)
        self.assertEquals(problem_12.Solution().get_highly_divisible_triangular_number(500), 76576500)

    def test_problem13(self):
        self.assertEquals(problem_13.Solution().get_large_sum('''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''), '5537376230')

    def test_problem14(self):
        self.assertEquals(problem_14.Solution().get_longest_collatz_sequence(1_000_000), 837799)

    def test_problem15(self):
        self.assertEquals(problem_15.Solution().get_lattice_paths(2), 6)
        self.assertEquals(problem_15.Solution().get_lattice_paths(20), 137846528820)

    def test_problem16(self):
        self.assertEquals(problem_16.Solution().get_power_digit_sum(15), 26)
        self.assertEquals(problem_16.Solution().get_power_digit_sum(1000), 1366)

    def test_problem17(self):
        self.assertEquals(problem_17.Solution().get_number_letter_counts(5), 19)
        self.assertEquals(problem_17.Solution().get_number_letter_counts(1000), 21124)

    def test_problem18(self):
        self.assertEquals(problem_18.Solution().get_maximum_path_sum_i(
            """3
            7 4
            2 4 6
            8 5 9 3"""
        ), 23)
        self.assertEquals(problem_18.Solution().get_maximum_path_sum_i(
            """75
            95 64
            17 47 82
            18 35 87 10
            20 04 82 47 65
            19 01 23 75 03 34
            88 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
            41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
            70 11 33 28 77 73 17 78 39 68 17 57
            91 71 52 38 17 14 91 43 58 50 27 29 48
            63 66 04 68 89 53 67 30 73 16 69 87 40 31
            04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
        ), 1074)

    def test_problem19(self):
        self.assertEquals(problem_19.Solution().get_counting_sundays(), 171)

    def test_problem20(self):
        self.assertEquals(problem_20.Solution().get_factorial_digit_sum(10), 27)
        self.assertEquals(problem_20.Solution().get_factorial_digit_sum(100), 648)

    def test_problem21(self):
        self.assertEquals(utils.sum_factors(15), 9)
        self.assertEquals(utils.sum_factors(25), 6)
        self.assertEquals(problem_21.Solution().sum_amicable_numbers(10000), 31626)

    def test_problem22(self):
        with open("resources/p022_names.txt", 'r') as content_file:
            content = content_file.read()
        self.assertEquals(problem_22.Solution().sum_names_scores(content), 871198282)

    def test_problem23(self):
        self.assertEquals(problem_23.Solution().sum_non_abudant_sums(28123), 4179871)

    def test_problem24(self):
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 0), "0123456789")
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 23688), "0167938542")
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 362880), "0987654321")
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 362881), "1023456789")
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 1000000), "2783915460")
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 1000001), "2783915604")
        self.assertEquals(problem_24.Solution().get_lexicographic_permutation(10, 3628800), "9876543210")

    def test_problem25(self):
        self.assertEquals(problem_25.Solution().get_n_digit_fibonacci_number(3), 12)
        self.assertEquals(problem_25.Solution().get_n_digit_fibonacci_number(4), 17)
        self.assertEquals(problem_25.Solution().get_n_digit_fibonacci_number(1000), 4782)

    def test_problem26(self):
        self.assertEquals(problem_26.Solution().get_max_recurring_cycle(10), 7)
        self.assertEquals(problem_26.Solution().get_max_recurring_cycle(100), 97)
        self.assertEquals(problem_26.Solution().get_max_recurring_cycle(1000), 983)

    def test_problem27(self):
        self.assertEquals(problem_27.Solution.get_quadratic_primes(1000, 1000), -59231)

    def test_problem28(self):
        self.assertEquals(problem_28.Solution.get_number_spiral_diagonals(1), 1)
        self.assertEquals(problem_28.Solution.get_number_spiral_diagonals(3), 25)
        self.assertEquals(problem_28.Solution.get_number_spiral_diagonals(5), 101)
        self.assertEquals(problem_28.Solution.get_number_spiral_diagonals(1001), 669171001)

    def test_problem29(self):
        self.assertEquals(problem_29.Solution.get_distinct_powers(5, 5), 15)
        self.assertEquals(problem_29.Solution.get_distinct_powers(100, 100), 9183)

    def test_problem30(self):
        self.assertEquals(problem_30.Solution.get_digit_fifth_powers(4), 19316)
        self.assertEquals(problem_30.Solution.get_digit_fifth_powers(5), 443839)

    def test_problem31(self):
        self.assertEquals(problem_31.Solution.get_coin_sums([1, 2, 5, 10, 20, 50, 100, 200], 200), 73682)

    def test_problem32(self):
        self.assertEquals(problem_32.Solution.get_pandigital_products(), 45228)

    def test_problem33(self):
        self.assertEquals(problem_33.Solution.get_digit_cancelling_fractions(), 100)

    def test_problem34(self):
        self.assertEquals(problem_34.Solution.get_digit_factorials(), 40730)

    def test_problem35(self):
        self.assertEquals(problem_35.Solution.get_circular_primes(100), 13)
        self.assertEquals(problem_35.Solution.get_circular_primes(1_000_000), 55)

    def test_problem36(self):
        self.assertEquals(problem_36.Solution.get_sum_of_double_based_palindromes(100), 157)
        self.assertEquals(problem_36.Solution.get_sum_of_double_based_palindromes(1_000_000), 872187)

    def test_problem37(self):
        self.assertEquals(problem_37.Solution.get_truncatable_primes(11), 748317)

    def test_problem38(self):
        self.assertEquals(problem_38.Solution.get_greatest_pandigital(), 932718654)

    def test_problem39(self):
        self.assertEquals(problem_39.Solution.get_max_solutions(1000), 840)

    def test_problem40(self):
        self.assertEquals(problem_40.Solution.get_champernownes_constant(), 210)

    def test_problem41(self):
        self.assertEquals(problem_41.Solution.find_largest_pandigital_prime(), 7652413)

    def test_problem42(self):
        with open("resources/p042_words.txt", 'r') as content_file:
            content = content_file.read()
            self.assertEquals(problem_42.Solution.get_number_of_coded_triangle_numbers(content), 162)

    def test_problem43(self):
        self.assertEquals(problem_43.Solution.get_sum_of_sub_string_divisible_pandigitals(), 16695334890)

    def test_problem44(self):
        self.assertEquals(problem_44.Solution.get_min_pentagon_distance(), 5482660)

    def test_problem45(self):
        self.assertEquals(problem_45.Solution.find_same_number(), 1533776805)

    def test_problem46(self):
        self.assertEquals(problem_46.Solution.get_goldbach_conjecture_min_contradiction(10_000), 5777)

    def test_problem47(self):
        self.assertEquals(problem_47.Solution.get_first_consequent_number(2), 14)
        self.assertEquals(problem_47.Solution.get_first_consequent_number(3), 644)
        self.assertEquals(problem_47.Solution.get_first_consequent_number(4), 134043)

    def test_problem48(self):
        self.assertEquals(problem_48.Solution.get_self_powers(10), "0405071317")
        self.assertEquals(problem_48.Solution.get_self_powers(1000), "9110846700")

    def test_problem49(self):
        self.assertEquals(problem_49.Solution.get_prime_permutations(), ['148748178147', '296962999629'])

    def test_problem53(self):
        self.assertEquals(problem_53.Solution.get_count_greater_than_mil(), 4075)

    def test_problem55(self):
        self.assertEquals(problem_55.Solution.get_lychrel_numbers_count(), 249)

    def test_problem57(self):
        self.assertEquals(problem_57.Solution.get_specific_square_root_convergents(100), 153)

    def test_problem58(self):
        self.assertEquals(problem_58.Solution.get_spiral_with_prime_ratio_below_10_ptc(), 26241)


