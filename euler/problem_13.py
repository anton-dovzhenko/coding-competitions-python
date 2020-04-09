class Solution:

    def get_large_sum(self, txt):
        digits = txt.split()
        s = 0
        for d in digits:
            d = d[0:12]
            s += int(d)
        return str(s)[0:10]

