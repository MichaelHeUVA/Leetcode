# https://leetcode.com/problems/binary-tree-paths/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []

        def backtrack(node, path):
            if not node:
                return
            if not node.left and not node.right:
                path.append(str(node.val))
                output.append(("->").join(path))
                path.pop()
                return

            path.append(str(node.val))
            backtrack(node.left, path)
            backtrack(node.right, path)
            path.pop()

        backtrack(root, [])
        return output
