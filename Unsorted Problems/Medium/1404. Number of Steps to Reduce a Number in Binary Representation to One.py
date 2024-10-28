# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
from collections import deque


# Simulation
class Solution:
    def numSteps(self, s: str) -> int:
        q = deque(s)
        output = 0

        def add_one(q):
            i = len(q) - 1
            while i >= 0 and q[i] == "1":
                q[i] = "0"
                i -= 1
            if i < 0:
                q.appendleft("1")
            else:
                q[i] = "1"

        def divide_by_two(q):
            q.pop()

        while len(q) > 1:
            if q[-1] == "1":
                add_one(q)
            else:
                divide_by_two(q)
            output += 1
        return output


# Convert string to number
class Solution:  # noqa F811
    def numSteps(self, s: str) -> int:
        output = 0
        num = int(s, 2)
        while num != 1:
            if num & 1 == 1:
                num += 1
            else:
                num = num >> 1
            output += 1
        return output
