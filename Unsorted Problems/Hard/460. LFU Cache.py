# https://leetcode.com/problems/lfu-cache/description/
from collections import defaultdict


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}

    def length(self):
        return len(self.map)

    def push(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val)

    def popleft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop(val)
        self.push(val)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0
        self.key_to_val = {}
        self.key_to_uses = defaultdict(int)
        self.list_map = defaultdict(LinkedList)

    def counter(self, key):
        count = self.key_to_uses[key]
        self.key_to_uses[key] += 1
        self.list_map[count].pop(key)
        self.list_map[count + 1].push(key)
        if count == self.lfu_count and self.list_map[count].length() == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self.counter(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.key_to_val and len(self.key_to_val) == self.capacity:
            res = self.list_map[self.lfu_count].popleft()
            self.key_to_val.pop(res)
            self.key_to_uses.pop(res)

        self.key_to_val[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.key_to_uses[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
