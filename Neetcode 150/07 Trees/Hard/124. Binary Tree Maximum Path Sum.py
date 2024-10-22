# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        def dfs(node):
            if not node:
                return 0

            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            # this is the max result with the split
            self.result = max(self.result, node.val + left_max + right_max)
            # return the max result without the split
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.result
