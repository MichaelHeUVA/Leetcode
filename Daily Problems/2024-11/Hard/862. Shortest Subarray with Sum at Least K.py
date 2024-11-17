# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/?envType=daily-question&envId=2024-11-17
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        output = float("inf")
        n = len(nums)
        current_sum = 0
        q = deque()

        for right in range(n):
            current_sum += nums[right]
            if current_sum >= k:
                output = min(output, right + 1)

            while q and current_sum - q[0][0] >= k:
                prefix, end_index = q.popleft()
                output = min(output, right - end_index)

            while q and q[-1][0] >= current_sum:
                q.pop()
            q.append((current_sum, right))

        return -1 if output == float("inf") else output
