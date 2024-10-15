# https://leetcode.com/problems/design-circular-deque/description/?envType=daily-question&envId=2024-09-28


class ListNode:
    def __init__(self, value: int):
        self.val = value
        self.prev = None
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if not self.front and not self.last:
            self.front = node
            self.last = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if not self.front and not self.last:
            self.front = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.front = None
            self.last = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.front = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.front.val if self.front else -1

    def getRear(self) -> int:
        return self.last.val if self.last else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
