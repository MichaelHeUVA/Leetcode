# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        group_prev = dummy_node

        while True:
            kth_node = self.getKthNode(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next

            prev = kth_node.next
            current = group_prev.next

            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp

        return dummy_node.next

    def getKthNode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
