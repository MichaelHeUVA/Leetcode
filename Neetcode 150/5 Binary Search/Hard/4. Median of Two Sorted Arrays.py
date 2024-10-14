# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        total = len(nums1) + len(nums2)
        left = 0
        right = len(nums1)
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1

            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            max_left = max(left1, left2)

            right1 = nums1[partition1] if partition1 < len(nums1) else float("inf")
            right2 = nums2[partition2] if partition2 < len(nums2) else float("inf")
            min_right = min(right1, right2)

            if max_left <= min_right:
                if total % 2:
                    return max_left
                return (max_left + min_right) / 2
            elif left1 > right2:
                right = partition1 - 1
            elif left2 > right1:
                left = partition1 + 1
