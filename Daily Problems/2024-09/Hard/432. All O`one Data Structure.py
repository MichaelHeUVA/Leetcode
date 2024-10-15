# https://leetcode.com/problems/all-oone-data-structure/?envType=daily-question&envId=2024-09-29


class ListNode:
    def __init__(self, count=None):
        self.keys = set()
        self.count = count
        self.next = None
        self.prev = None


class AllOne:
    def __init__(self):
        self.min = ListNode(0)
        self.max = ListNode(0)
        self.max.prev = self.min
        self.min.next = self.max
        self.map = {}  # map key to listnode

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            count = node.count
            node.keys.remove(key)

            next_node = node.next
            # Create a new node if the next node is the max or the next node isn't count + 1
            if next_node == self.max or next_node.count != count + 1:
                new_node = ListNode(count + 1)
                new_node.keys.add(key)
                new_node.prev = node
                new_node.next = next_node
                node.next = new_node
                next_node.prev = new_node
                self.map[key] = new_node
            # Add the key to the next node's set
            else:
                next_node.keys.add(key)
                self.map[key] = next_node

            # Remove the current node if there aren't any keys in the set
            if not node.keys:
                self.removeNode(node)
        # Not in the map
        else:
            min_node = self.min.next
            # If the next node doesn't exist or if the min_node's count is greater than 1
            if min_node == self.max or min_node.count > 1:
                node = ListNode(1)
                node.keys.add(key)
                node.prev = self.min
                node.next = min_node
                self.min.next = node
                min_node.prev = node
                self.map[key] = node
            else:
                min_node.keys.add(key)
                self.map[key] = min_node

    def dec(self, key: str) -> None:
        node = self.map[key]
        node.keys.remove(key)
        count = node.count

        # If the count is only one remove the node from the map
        if count == 1:
            del self.map[key]
        else:
            prev_node = node.prev
            # Create a new node if the previous node doesn't exist or if the count of the previous node is not 1 less
            if prev_node == self.min or prev_node.count != count - 1:
                new_node = ListNode(count - 1)
                new_node.keys.add(key)
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                self.map[key] = new_node
            else:
                prev_node.keys.add(key)
                self.map[key] = prev_node
        # Remove the node if the set is empty
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.max.prev != self.min:
            return list(self.max.prev.keys)[0]
        return ""

    def getMinKey(self) -> str:
        if self.min.next != self.max:
            return list(self.min.next.keys)[0]
        return ""

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
