class Solution:

    def get_lexicographic_permutation(self, n, k):
        digits = list(range(0, n))

        if k == 0:
            return ''.join(list(map(str, digits)))

        divisors = [1]
        indices = []
        ordered = []

        for i in range(2, n):
            divisors.append(divisors[-1] * i)

        while k > 0:
            r = k % divisors[-1]
            i = int((k - r) / divisors[-1])
            if r == 0 and i > 0:
                i -= 1
            indices.append(i)
            divisors = divisors[:-1]
            k = r

        for i in indices:
            ordered.append(digits[i])
            digits.remove(digits[i])

        # reversed order because '0' remainder means last element
        ordered += reversed(digits)
        return ''.join(list(map(str, ordered)))
