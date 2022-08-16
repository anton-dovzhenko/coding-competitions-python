import unittest


class Solution:

    def smallestNumber(self, pattern: str):
        pattern = pattern[0] + pattern
        p = [pattern[0]]
        pc = [1]
        queue = [str(i) for i in range(1, len(pattern) + 1)]
        result = []
        for i in range(1, len(pattern)):
            if pattern[i] == p[-1]:
                pc[-1] += 1
            else:
                p.append(pattern[i])
                pc.append(1)

        for i in range(len(p) - 1):
            if p[i] == 'I':
                result += queue[0:pc[i] - 1]
                queue = queue[pc[i] - 1:]
                result += [queue[pc[i + 1]]]
                queue.remove(result[-1])
            else:
                result += reversed(queue[0:pc[i]])
                queue = queue[pc[i]:]
        if p[-1] == 'I':
            result += queue
        else:
            result += reversed(queue)

        return ''.join(result)


class SolutionTest(unittest.TestCase):

    def test_edgeScore(self):
        self.assertEqual(Solution().smallestNumber('IIIDIDDD'), '123549876')
        self.assertEqual(Solution().smallestNumber('DDD'), '4321')




