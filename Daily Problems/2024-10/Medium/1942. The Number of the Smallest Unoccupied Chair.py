# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/?envType=daily-question&envId=2024-10-11
from heapq import heappush, heappop
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = []
        # heap to keep track of empty chairs
        friend_arriving_time = times[targetFriend][0]
        times.sort()
        end_times = []
        given_seat = 0
        for start, end in times:
            # when people leave free the chair
            while end_times and end_times[0][0] <= start:
                _, chair = heappop(end_times)
                heappush(chairs, chair)
            if not chairs:
                given_seat = len(end_times)
            else:
                given_seat = heappop(chairs)
            heappush(end_times, (end, given_seat))
            if start == friend_arriving_time:
                break
        return given_seat
