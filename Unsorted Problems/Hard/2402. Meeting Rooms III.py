# https://leetcode.com/problems/meeting-rooms-iii/description/
from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_uses = [0] * n
        free_rooms = [i for i in range(n)]
        used_rooms = []
        meetings.sort()

        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                heappush(free_rooms, heappop(used_rooms)[1])

            if free_rooms:
                room = heappop(free_rooms)
                heappush(used_rooms, (end, room))
            else:
                end_time, room = heappop(used_rooms)
                heappush(used_rooms, (end_time + (end - start), room))

            room_uses[room] += 1

        return room_uses.index(max(room_uses))
