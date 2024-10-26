# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/?envType=daily-question&envId=2024-10-26
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}
        max_removal = {}

        def maxHeight(node):
            if not node:
                return -1
            if node.val in heights:
                return heights[node.val]
            heights[node.val] = max(maxHeight(node.left), maxHeight(node.right)) + 1
            return heights[node.val]

        def dfs(node, depth, max_val):
            if not node:
                return
            max_removal[node.val] = max_val

            dfs(node.left, depth + 1, max(max_val, depth + 1 + maxHeight(node.right)))

            dfs(node.right, depth + 1, max(max_val, depth + 1 + maxHeight(node.left)))

        dfs(root, 0, 0)
        return [max_removal[q] for q in queries]
