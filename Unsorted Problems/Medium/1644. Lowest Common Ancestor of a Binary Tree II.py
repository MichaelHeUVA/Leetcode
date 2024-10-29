# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        lca = None

        def dfs(node):
            nonlocal lca
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node.val == p.val or node.val == q.val
            if (mid and (left or right)) or (left and right):
                lca = node
            return mid or left or right

        dfs(root)
        return lca
