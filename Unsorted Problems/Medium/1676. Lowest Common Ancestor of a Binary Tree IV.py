# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        nodes = set(nodes)
        lca = None

        def dfs(node):
            nonlocal lca
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node in nodes
            if left and right or (mid and not (left and right)):
                lca = node
            return mid or left or right

        dfs(root)
        return lca
