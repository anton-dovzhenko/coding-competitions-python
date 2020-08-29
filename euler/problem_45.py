class Solution:

    @classmethod
    def find_same_number(cls):
        t = 285
        p = 165
        h = 144
        tn = 40755
        pn = 40755
        hn = 41328

        while True:
            if tn == pn and pn == hn:
                # print("t=%s p=%s h=%s" %(t, p, h))
                return int(tn)
            elif tn <= pn and tn <= hn:
                t += 1
                tn = t * (t + 1) / 2
            elif pn <= tn and pn <= hn:
                p += 1
                pn = p * (3 * p - 1) / 2
            else:
                h += 1
                hn = h * (2 * h - 1)

