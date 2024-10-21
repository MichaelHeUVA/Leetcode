# https://leetcode.com/problems/detect-squares/description/
from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.frequency = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.frequency[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        for x, y in list(self.frequency):
            if abs(px - x) == abs(py - y) and (px != x and py != y):
                count += (
                    self.frequency[(x, py)]
                    * self.frequency[(px, y)]
                    * self.frequency[(x, y)]
                )
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
