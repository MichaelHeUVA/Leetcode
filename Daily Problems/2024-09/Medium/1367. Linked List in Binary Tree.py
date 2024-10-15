# https://leetcode.com/problems/linked-list-in-binary-tree/description/?envType=daily-question&envId=2024-09-07
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if not node:
                return False
            if node.val == val:
                pointer = head
                return (
                    dfsList(node, pointer)
                    or dfs(node.left, val)
                    or dfs(node.right, val)
                )
            return dfs(node.left, val) or dfs(node.right, val)

        def dfsList(node, pointer):
            if not node:
                return False
            if node.val != pointer.val:
                return False
            if not pointer.next:
                return True
            return dfsList(node.left, pointer.next) or dfsList(node.right, pointer.next)

        return dfs(root, head.val)
