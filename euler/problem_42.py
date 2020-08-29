class Solution:

    @classmethod
    def get_number_of_coded_triangle_numbers(cls, s):
        triangle_count = 0
        l = 0
        i = 0
        for c in s.split(','):
            c = c[1:-1]
            score = cls.get_word_score(c)
            if cls.is_triangle(score):
                triangle_count += 1
        return triangle_count

    @classmethod
    def get_word_score(cls, word):
        score = 0
        for c in word:
            score += ord(c) - ord('A') + 1
        return score

    @classmethod
    def is_triangle(cls, n):
        return (((1 + 4 * n * 2) ** 0.5 - 1) / 2).is_integer()


# print(Solution.get_number_of_coded_triangle_numbers('"A","ABILITY","ABLE","ABOUT","ABOVE","ABSENCE","ABSOLUTELY"'))
# print(Solution.get_number_of_coded_triangle_numbers('"SKY"'))
