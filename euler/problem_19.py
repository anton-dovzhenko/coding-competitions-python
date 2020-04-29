import math


class Solution:

    def _get_days(self, y, m):
        # Dec is 0, Jan is 1, ..., Nov is 11
        if m in [0, 1, 3, 5, 7, 8, 10]:
            return 31
        elif m in [4, 6, 9, 11]:
            return 30
        else:
            return 28 if y % 4 != 0 or y % 400 == 0 else 29

    def get_counting_sundays(self):
        cnt = 0
        start = 1
        for i in range(1, 101 * 12):
            y = math.floor(i / 12)
            m = i % 12
            d = self._get_days(y, m)
            start += d
            if start % 7 == 0 and y > 0:
                cnt += 1
        return cnt

