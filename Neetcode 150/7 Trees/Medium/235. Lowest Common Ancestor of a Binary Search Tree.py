# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
                return
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                lca = node
                return
            if node.val < p.val and node.val < q.val:
                dfs(node.right)
            if q.val < node.val and p.val < node.val:
                dfs(node.left)

        dfs(root)
        return lca
