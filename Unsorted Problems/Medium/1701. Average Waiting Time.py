# https://leetcode.com/problems/average-waiting-time/description/
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        end_time = 0
        total_time = 0
        n = len(customers)
        for arrival, time in customers:
            if end_time < arrival:
                total_time += time
                end_time = arrival + time
            else:
                end_time += time
                total_time += end_time - arrival
        return total_time / n
