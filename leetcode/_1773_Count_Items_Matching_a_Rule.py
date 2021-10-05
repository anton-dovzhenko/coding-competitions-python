import unittest


class Solution:

    def countMatches(self, items, ruleKey, ruleValue):
        i = ["type", "color", "name"].index(ruleKey)
        return sum(ruleValue == x[i] for x in items)


class SolutionTest(unittest.TestCase):

    def test_countMatches(self):
        self.assertEquals(Solution().countMatches([["phone", "blue", "pixel"],
                                                   ["computer", "silver", "lenovo"],
                                                   ["phone", "gold", "iphone"]],
                                                  "color", "silver"), 1)
        self.assertEquals(Solution().countMatches([["phone", "blue", "pixel"],
                                                   ["computer", "silver", "phone"],
                                                   ["phone", "gold", "iphone"]],
                                                  "type", "phone"), 2)

