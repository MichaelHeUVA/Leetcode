# https://leetcode.com/problems/first-unique-number/description/
from collections import Counter, defaultdict, deque
from typing import List


# Dictionary and Queue
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.counts = defaultdict(int)
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue:
            if self.counts[self.queue[0]] == 1:
                return self.queue[0]
            else:
                self.queue.popleft()

        return -1

    def add(self, value: int) -> None:
        self.counts[value] += 1
        if self.counts[value] == 1:
            self.queue.append(value)


# Counter
class FirstUnique:  # noqa: F811
    def __init__(self, nums: List[int]):
        self.counts = Counter(nums)

    def showFirstUnique(self) -> int:
        for key in self.counts:
            if self.counts[key] == 1:
                return key
        return -1

    def add(self, value: int) -> None:
        self.counts[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
