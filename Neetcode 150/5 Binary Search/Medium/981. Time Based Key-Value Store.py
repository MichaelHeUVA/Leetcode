# https://leetcode.com/problems/time-based-key-value-store/description/
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        keys = self.map[key]
        result = ""
        left, right = 0, len(keys) - 1
        while left <= right:
            mid = (left + right) // 2
            if keys[mid][0] <= timestamp:
                result = keys[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
