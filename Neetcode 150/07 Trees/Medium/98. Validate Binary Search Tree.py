# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True

            if not low < node.val < high:
                return False

            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root, float("-inf"), float("inf"))
