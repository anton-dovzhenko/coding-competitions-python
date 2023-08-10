import unittest


class Solution:
    def finalString(self, s: str) -> str:
        result = []
        inversed = False
        for c in s:
            if c == 'i':
                inversed = not inversed
            elif inversed:
                result.insert(0, c)
            else:
                result.append(c)

        if inversed:
            result = reversed(result)
        return ''.join(result)

class SolutionTest(unittest.TestCase):

    def test_finalString(self):
        self.assertEqual(Solution().finalString("string"), "rtsng")
        self.assertEqual(Solution().finalString("poiinter"), "ponter")


