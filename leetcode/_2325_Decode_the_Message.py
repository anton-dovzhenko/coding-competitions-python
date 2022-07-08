import unittest


class Solution:

    def decodeMessage(self, key: str, message: str) -> str:
        decoder = {' ': ' '}
        i = 0
        for k in key:
            if k not in decoder:
                decoder[k] = chr(ord('a') + i)
                i += 1
        return ''.join(decoder[x] for x in message)


class SolutionTest(unittest.TestCase):

    def test_maximumsSplicedArray(self):
        self.assertEqual(Solution().decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"),
                         "this is a secret")
        self.assertEqual(Solution().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"),
                         "the five boxing wizards jump quickly")


