# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/?envType=daily-question&envId=2024-10-22
from collections import deque
from heapq import heappush, heappushpop
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        max_heap = []
        q = deque([root])

        while q:
            size = len(q)
            level_sum = 0
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(max_heap) == k:
                heappushpop(max_heap, level_sum)
            else:
                heappush(max_heap, level_sum)

        return max_heap[0] if len(max_heap) == k else -1
