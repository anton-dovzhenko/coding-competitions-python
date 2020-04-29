class Solution:

    def __init__(self):
        self.d = {"0": "", "00": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
             "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
             "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
             "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen", "20": "twenty",
             "30": "thirty", "40": "forty", "50": "fifty", "60": "sixty",
             "70": "seventy", "80": "eighty", "90": "ninety", "100": "hundred", "1000": "thousand"}
        self.d = {k: len(v) for k, v in self.d.items()}

    def get_number_letter_counts(self, n):
        ss = 0
        for i in range(1, n + 1):
            ns = str(i).zfill(4)
            s = 0
            a = i % 100
            b = (i - a) % 1000
            c = i - b - a
            if a > 0:
                s += self.d[ns[2:4]] if ns[2:4] in self.d else self.d[ns[-2] + "0"] + self.d[ns[-1]]
            if b > 0:
                s += self.d[ns[-3]] + self.d["100"]
            if c > 0:
                s += self.d[ns[-4]] + self.d["1000"]
            if a > 0 and (b > 0 or c > 0):
                s += len("and")
            ss += s
        return ss


