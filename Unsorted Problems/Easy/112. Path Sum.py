# https://leetcode.com/problems/path-sum/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum):
            if not node:
                return False
            sum += node.val
            if sum == targetSum and not node.left and not node.right:
                return True
            return dfs(node.left, sum) or dfs(node.right, sum)

        return dfs(root, 0)
