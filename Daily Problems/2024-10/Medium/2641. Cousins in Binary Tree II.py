# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/?envType=daily-question&envId=2024-10-23
from collections import deque, defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root, None)])

        while q:
            size = len(q)
            level_sum = sum(map(lambda x: x[0].val, q))
            level = []

            for _ in range(size):
                node, parent = q.popleft()
                level.append((node, parent))
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            parent_sum = defaultdict(int)
            for node, parent in level:
                parent_sum[parent] += node.val

            for node, parent in level:
                node.val = level_sum - parent_sum[parent]

        return root
