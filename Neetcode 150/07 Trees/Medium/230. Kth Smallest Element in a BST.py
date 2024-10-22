# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0

        def inorder(node):
            nonlocal k, num
            if not node:
                return

            inorder(node.left)
            k -= 1
            if not k:
                num = node.val
                return
            inorder(node.right)

        inorder(root)
        return num
