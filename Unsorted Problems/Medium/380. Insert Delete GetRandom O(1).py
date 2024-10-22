# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
from collections import defaultdict
from random import choice


class RandomizedSet:
    def __init__(self):
        self.map = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            if len(self.list) == 1 or self.map[val] == len(self.list) - 1:
                self.list.pop()
                del self.map[val]
                return True
            # pop off the right most element and swap it with the removed element
            index = self.map[val]
            right_element = self.list.pop()
            self.list[index] = right_element
            self.map[right_element] = index
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
