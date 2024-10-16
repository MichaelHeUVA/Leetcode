# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        left_tree_inorder = inorder[:mid]
        left_tree_preorder = preorder[1 : mid + 1]
        right_tree_inorder = inorder[mid + 1 :]
        right_tree_preorder = preorder[mid + 1 :]
        root.left = self.buildTree(left_tree_preorder, left_tree_inorder)
        root.right = self.buildTree(right_tree_preorder, right_tree_inorder)

        return root
