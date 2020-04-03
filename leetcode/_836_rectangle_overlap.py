import unittest


class Solution:

    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[0] >= rec2[2] or rec2[0] >= rec1[2]
                    or rec1[1] >= rec2[3] or rec2[1] >= rec1[3])


class SolutionTest(unittest.TestCase):

    def test_isRectangleOverlap(self):
        self.assertTrue(Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
        self.assertFalse(Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))


