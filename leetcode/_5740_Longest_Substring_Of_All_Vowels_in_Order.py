class Solution:

    def longestBeautifulSubstring(self, word):
        d = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        max_length = 0
        length = 0
        used = -1
        for c in word:
            order = d[c]
            if order == used or order == used + 1:
                length += 1
                used = order
            else:
                if used == 4:
                    max_length = max(max_length, length)
                if order == 0:
                    length = 1
                    used = 0
                else:
                    length = 0
                    used = -1
        if used == 4:
            max_length = max(max_length, length)
        return max_length


print(Solution().longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
print(Solution().longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
print(Solution().longestBeautifulSubstring("a"))