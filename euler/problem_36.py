class Solution:

    @classmethod
    def get_sum_of_double_based_palindromes(cls, N):
        s = 0
        for n in range(0, N):
            if cls.is_palindrome(str(n)) and cls.is_palindrome(bin(n)[2:]):
                s += n
        return s

    @classmethod
    def is_palindrome(cls, s: str):
        for i in range(0, int(len(s) / 2)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


