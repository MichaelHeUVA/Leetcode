# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        output = []
        window = 0
        left = 1
        right = k
        if k < 0:
            left = n - abs(k)
            right = n - 1
        for i in range(left, right + 1):
            window += code[i]

        for i in range(n):
            output.append(window)
            window += code[(right + 1) % n]
            window -= code[left % n]
            left += 1
            right += 1

        return output
