# https://leetcode.com/problems/balance-a-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)

        def buildBalancedBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = nodes[mid]

            node.left = buildBalancedBST(left, mid - 1)
            node.right = buildBalancedBST(mid + 1, right)
            return node

        return buildBalancedBST(0, len(nodes) - 1)
