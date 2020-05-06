class Solution:

    def sum_amicable_numbers(self, n):
        s = 0
        d = {}
        for i in range(1, n):
            d[i] = self.sum_factors(i)

        for key, value in d.items():
            if key != value and value in d and d[value] == key:
                s += key + value

        return int (s / 2)

    def sum_factors(self, n):
        s = 1
        rt = int(n ** 0.5)
        for i in range(2, rt + 1):
            if n % i == 0:
                s += i + (0 if i == n / i else n / i)
        return int(s)

