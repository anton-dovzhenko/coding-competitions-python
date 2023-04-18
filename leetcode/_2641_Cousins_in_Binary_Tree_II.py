# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [root]
        root.val = 0
        while len(level) > 0:
            next_level = []
            level_sum = 0
            for node in level:
                next_level.append(node.left)
                next_level.append(node.right)
                level_sum += 0 if node.left is None else node.left.val
                level_sum += 0 if node.right is None else node.right.val
            level = []
            for i in range(0, len(next_level) // 2):
                i1 = 2 * i
                i2 = 2 * i + 1
                node_score = level_sum - (0 if next_level[i1] is None else next_level[i1].val) - (0 if next_level[i2] is None else next_level[i2].val)
                if next_level[i1] is not None:
                    next_level[i1].val = node_score
                    level.append(next_level[i1])
                if next_level[i2] is not None:
                    next_level[i2].val = node_score
                    level.append(next_level[i2])
        return root





