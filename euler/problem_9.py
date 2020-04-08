class Solution:

    def get_special_pythagorean_triplet(self, s):
        for a in range(1, s):
            for b in range(a + 1, s):
                c = s - a - b
                diff = c ** 2 - a ** 2 - b ** 2
                if diff < 0:
                    break
                elif diff == 0:
                    return a * b * c
        return None


print(Solution().get_special_pythagorean_triplet(12))
print(Solution().get_special_pythagorean_triplet(1000))


