import unittest
import math


class Solution:

    def ladderLength(self, beginWord, endWord, wordList) -> int:
        length = self._ladderLength([beginWord], endWord, wordList)
        return 0 if math.isinf(length) else length

    def _ladderLength(self, beginWords, endWord, wordList) -> int:
        if endWord in beginWords:
            return 1
        if endWord not in wordList or len(beginWords) == 0:
            return float('inf')

        next_begin_words = []
        next_word_list = []
        for i in range(0, len(wordList)):
            w = wordList[i]
            is_bw = False
            for bw in beginWords:
                if self._one_change(bw, w):
                    next_begin_words.append(w)
                    is_bw = True
                    break
            if not is_bw:
                next_word_list.append(w)

        return 1 + self._ladderLength(next_begin_words, endWord, next_word_list)

    def _one_change(self, a, b):
        c = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                c += 1
            if c > 1:
                return False
        return True


class Solution2:

    def ladderLength(self, beginWord, endWord, wordList) -> int:
        d = {}
        for w in wordList:
            for i in range(0, len(w)):
                key = w[:i] + '.' + w[i + 1:]
                if key not in d:
                    d[key] = []
                d[key].append(w)
        length = self._ladderLength([beginWord], endWord, d)
        return 0 if math.isinf(length) else length

    def _ladderLength(self, begin_words, end_word, d) -> int:
        if end_word in begin_words:
            return 1
        if len(begin_words) == 0 or len(d) == 0:
            return float('inf')
        next_begin_words = []
        for bw in begin_words:
            for i in range(0, len(bw)):
                key = bw[:i] + '.' + bw[i + 1:]
                if key in d:
                    next_begin_words = next_begin_words + d[key]
                    del d[key]

        return 1 + self._ladderLength(next_begin_words, end_word, d)



class SolutionTest(unittest.TestCase):

    def test_ladderLength1(self):
        self.assertEquals(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEquals(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
        self.assertEquals(Solution().ladderLength("hot", "dog", ["hot", "dog"]), 0)

    def test_ladderLength2(self):
        self.assertEquals(Solution2().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEquals(Solution2().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
        self.assertEquals(Solution2().ladderLength("hot", "dog", ["hot", "dog"]), 0)

