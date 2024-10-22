# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        output = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

        dfs(root)
        return output
