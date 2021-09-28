import unittest


class Solution:

    def findRadius(self, houses, heaters):
        heaters.sort()
        houses.sort()
        radius = 0
        heat = 0
        for h in houses:
            while heat < len(heaters) - 1 and heaters[heat + 1] <= h:
                heat += 1
            r = abs(h - heaters[heat])
            if heat < len(heaters) - 1:
                r = min(r, heaters[heat + 1] - h)
            radius = max(radius, r)
        return radius


class SolutionTest(unittest.TestCase):

    def test_findRadius(self):
        self.assertEquals(Solution().findRadius([1, 2, 3], [2]), 1)
        self.assertEquals(Solution().findRadius([1, 2, 3, 4], [1, 4]), 1)
        self.assertEquals(Solution().findRadius([1, 5], [2]), 3)
        self.assertEquals(Solution().findRadius([1, 5], [10]), 9)


