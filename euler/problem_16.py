class Solution:

    def get_power_digit_sum(self, n):
        digits = 2 ** n
        digits = str(digits)
        _sum = 0
        for d in digits:
            _sum += ord(d) - ord('0')
        return _sum

