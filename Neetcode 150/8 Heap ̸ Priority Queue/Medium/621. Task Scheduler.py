# https://leetcode.com/problems/task-scheduler/description/
from collections import Counter, deque
from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapify(max_heap)

        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1
            if max_heap:
                frequency = 1 + heappop(max_heap)
                if frequency:
                    queue.append([frequency, time + n])
            if queue and queue[0][1] == time:
                heappush(max_heap, queue.popleft()[0])

        return time
