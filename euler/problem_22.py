class Solution:

    def sum_names_scores(self, txt):
        txt = txt.split(",")
        txt.sort()
        s = 0
        score_adj = -2 * (ord('"') - ord('A') + 1)
        for i in range(0, len(txt)):
            name = txt[i]
            score = 0
            for c in name:
                score += ord(c) - ord('A') + 1
            score += score_adj
            score *= i + 1
            s += score
        return s

