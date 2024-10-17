# https://leetcode.com/problems/maximum-swap/description/?envType=daily-question&envId=2024-10-17


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, str(num)))
        max_at_index = len(nums) - 1
        small = 0
        large = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[max_at_index] < nums[i]:
                max_at_index = i
            elif nums[i] < nums[max_at_index]:
                small = i
                large = max_at_index

        nums[small], nums[large] = nums[large], nums[small]
        return int("".join(map(str, nums)))
