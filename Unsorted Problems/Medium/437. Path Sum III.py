# https://leetcode.com/problems/path-sum-iii/description/
from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = 0
        prefix_sum = defaultdict(int)

        def dfs(node, path_sum):
            nonlocal paths
            if not node:
                return

            path_sum += node.val

            if path_sum == targetSum:
                paths += 1

            paths += prefix_sum[path_sum - targetSum]

            prefix_sum[path_sum] += 1

            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

            prefix_sum[path_sum] -= 1

        dfs(root, 0)
        return paths
