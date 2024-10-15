# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10
import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head.next:
            return head
        prev = head
        output = head
        head = head.next
        while head:
            gcd = math.gcd(prev.val, head.val)
            prev.next = ListNode(gcd, head)
            prev = head
            head = head.next
        return output
