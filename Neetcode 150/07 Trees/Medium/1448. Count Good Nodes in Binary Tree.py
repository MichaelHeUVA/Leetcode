# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                self.count += 1
            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))

        dfs(root, root.val)
        return self.count
