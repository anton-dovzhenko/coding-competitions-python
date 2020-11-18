import unittest


class Solution:

    def findLadders(self, beginWord, endWord, wordList):
        d = {}
        for w in wordList:
            for i in range(0, len(w)):
                key = w[:i] + '.' + w[i + 1:]
                if key not in d:
                    d[key] = []
                d[key].append(w)
        result = self._find_ladders([[beginWord]], endWord, d)
        result = [line for line in result if line[-1] == endWord]
        return result

    def _find_ladders(self, sequences, end_word, d):
        if len(sequences) == 0 or len(d) == 0:
            return sequences

        begin_words = {}
        for line in sequences:
            word = line[-1]
            if word == end_word:
                return sequences
            for i in range(0, len(word)):
                key = word[:i] + '.' + word[i + 1:]
                if key in d:
                    if key not in begin_words:
                        begin_words[key] = []
                    begin_words[key].append(line)

        next_sequences = []
        for key, value in begin_words.items():
            words = d[key]
            for line in value:
                for word in words:
                    next_sequences.append(line + [word])
            del d[key]

        return self._find_ladders(next_sequences, end_word, d)


class SolutionTest(unittest.TestCase):

    def test_ladderLength1(self):
        self.assertEquals(Solution().findLadders("a", "c", ["a", "b", "c"]), [['a', 'c']])
        self.assertEquals(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
                          [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']])
        self.assertEquals(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), [])

