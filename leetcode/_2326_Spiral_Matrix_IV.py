# Definition for singly-linked list.
import unittest

import numpy as np
from typing import Optional, List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        if len(values) == 0:
            return None
        head = ListNode(values[0])
        cursor = head
        for i in range(1, len(values)):
            cursor.next = ListNode(values[i])
            cursor = cursor.next
        return head


class Solution:

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = np.full((m, n), -1)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_dir = 0
        pos = [0, 0]
        while head is not None:
            matrix[pos[0]][pos[1]] = head.val
            dir = directions[current_dir]
            next_pos = [pos[0] + dir[0], pos[1] + dir[1]]
            if (not (0 <= next_pos[0] < m and 0 <= next_pos[1] < n)) or matrix[next_pos[0]][next_pos[1]] != -1:
                current_dir = (current_dir + 1) % 4
                dir = directions[current_dir]
                next_pos = [pos[0] + dir[0], pos[1] + dir[1]]
            pos = next_pos
            head = head.next
        return matrix.tolist()


class SolutionTest(unittest.TestCase):

    def test_maximumsSplicedArray(self):
        self.assertEqual(Solution().spiralMatrix(3, 5, ListNode.from_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])),
                         [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]])
        self.assertEqual(Solution().spiralMatrix(1, 4, ListNode.from_list([0, 1, 2])), [[0, 1, 2, -1]])
