# https://leetcode.com/problems/prime-subtraction-operation/description/?envType=daily-question&envId=2024-11-11
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)

        def create_primes(x):
            is_prime = [True] * (x + 1)
            primes = []
            for p in range(2, x + 1):
                if is_prime[p]:
                    primes.append(p)
                    for i in range(p * p, x + 1, p):
                        is_prime[i] = False
            return primes

        primes = create_primes(max(nums))
        prev = float("-inf")
        for i in range(n):
            left = 0
            right = len(primes) - 1
            k = 0
            while left <= right:
                mid = (left + right) // 2
                if primes[mid] < nums[i] and prev < nums[i] - primes[mid]:
                    k = primes[mid]
                    left = mid + 1
                else:
                    right = mid - 1
            nums[i] -= k
            prev = nums[i]
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                return False
        return True
