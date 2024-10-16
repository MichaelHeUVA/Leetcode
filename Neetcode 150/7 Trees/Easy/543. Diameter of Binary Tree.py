# https://leetcode.com/problems/diameter-of-binary-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def dfs(node):
            nonlocal max_length
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            max_length = max(max_length, left_height + right_height)
            return max(left_height, right_height) + 1

        dfs(root)
        return max_length
