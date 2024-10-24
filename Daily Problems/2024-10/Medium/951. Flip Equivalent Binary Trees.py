# https://leetcode.com/problems/flip-equivalent-binary-trees/description/?envType=daily-question&envId=2024-10-24
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            left1 = node1.left.val if node1.left else None
            left2 = node2.left.val if node2.left else None
            right1 = node1.right.val if node1.right else None
            right2 = node2.right.val if node2.right else None
            if left1 == left2 and right1 == right2:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            elif left1 == right2 and right1 == left2:
                return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            else:
                return False

        return dfs(root1, root2)
