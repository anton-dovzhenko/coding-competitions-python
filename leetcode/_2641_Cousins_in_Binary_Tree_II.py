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
            level_sums = [level_sum] * len(next_level)
            for i in range(0, len(next_level)):
                if i % 2 == 0:
                    if next_level[i] is not None:
                        level_sums[i] -= next_level[i].val + (0 if next_level[i + 1] is None else next_level[i + 1].val)
                else:
                    if next_level[i] is not None:
                        level_sums[i] -= next_level[i].val + (0 if next_level[i - 1] is None else next_level[i - 1].val)
            level = []
            for i in range(0, len(next_level)):
                if next_level[i] is not None:
                    next_level[i].val = level_sums[i]
                    level.append(next_level[i])

        return root





