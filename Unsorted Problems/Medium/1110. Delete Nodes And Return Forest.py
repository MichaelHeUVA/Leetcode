# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        delete = set(to_delete)
        output = []

        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in delete:
                if node.left:
                    output.append(node.left)
                if node.right:
                    output.append(node.right)
                return None
            return node

        root = dfs(root)

        if root:
            output.append(root)
        return output
