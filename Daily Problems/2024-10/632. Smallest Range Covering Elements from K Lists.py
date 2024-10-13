# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/?envType=daily-question&envId=2024-10-13
from collections import defaultdict
from typing import List


# Merging sorting and minium window substring
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)

        merged_list = []
        for i in range(len(nums)):
            for num in nums[i]:
                merged_list.append((num, i))

        merged_list.sort()

        n = len(merged_list)
        output = [0, float("inf")]
        window_map = defaultdict(int)
        count = 0
        left = 0
        for right in range(n):
            window_map[merged_list[right][1]] += 1
            if window_map[merged_list[right][1]] == 1:
                count += 1

            while count == k:
                current_range = merged_list[right][0] - merged_list[left][0]
                if current_range < output[1] - output[0]:
                    output[0] = merged_list[left][0]
                    output[1] = merged_list[right][0]
                window_map[merged_list[left][1]] -= 1
                if window_map[merged_list[left][1]] == 0:
                    count -= 1
                left += 1
        return output


# Priority Queue
from heapq import heappush, heappop  # noqa: E402


class Solution:  # noqa: F811
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        pq = []

        max_num = float("-inf")
        for i in range(k):
            heappush(pq, (nums[i][0], i, 0))
            max_num = max(max_num, nums[i][0])

        output = [0, float("inf")]
        while len(pq) == k:
            min_num, i, j = heappop(pq)

            if max_num - min_num < output[1] - output[0]:
                output[0] = min_num
                output[1] = max_num

            if j + 1 < len(nums[i]):
                next_num = nums[i][j + 1]
                heappush(pq, (next_num, i, j + 1))
                max_num = max(max_num, next_num)

        return output
