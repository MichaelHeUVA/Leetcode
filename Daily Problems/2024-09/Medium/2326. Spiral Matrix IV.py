# https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left = 0
        right = n
        top = 0
        bot = m
        output = [[-1] * n for _ in range(m)]
        while left < right and top < bot and head:
            for i in range(left, right):
                if head:
                    output[top][i] = head.val
                    head = head.next
            top += 1
            for i in range(top, bot):
                if head:
                    output[i][right - 1] = head.val
                    head = head.next
            right -= 1
            for i in range(right - 1, left - 1, -1):
                if head:
                    output[bot - 1][i] = head.val
                    head = head.next
            bot -= 1
            for i in range(bot - 1, top - 1, -1):
                if head:
                    output[i][left] = head.val
                    head = head.next
            left += 1

        return output
