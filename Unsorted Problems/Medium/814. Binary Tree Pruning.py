# https://leetcode.com/problems/binary-tree-pruning/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def remove_node(node):
            if not node:
                return False
            if remove_node(node.left):
                node.left = None
            if remove_node(node.right):
                node.right = None
            if not node.left and not node.right and node.val == 0:
                return True

        if remove_node(root):
            return None
        return root
