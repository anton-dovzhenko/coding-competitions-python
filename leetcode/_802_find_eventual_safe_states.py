import unittest


class Solution:

    def eventualSafeNodes(self, graph):
        R = range(0, len(graph))
        link_count = [len(x) for x in graph]

        graph_rev = {}
        for i in R:
            graph_rev[i] = []

        for i in R:
            for n in graph[i]:
                graph_rev[n].append(i)

        progress = True
        terminal = []

        while progress:
            progress = False
            for i in R:
                if link_count[i] == 0:
                    terminal.append(i)
                    for n in graph_rev[i]:
                        progress = True
                        link_count[n] -= 1
                    link_count[i] = -1

        terminal.sort()
        return terminal


class SolutionTest(unittest.TestCase):

    def test_eventualSafeNodes(self):
        self.assertEquals(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]), [2, 4, 5, 6])