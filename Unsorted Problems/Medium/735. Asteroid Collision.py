# https://leetcode.com/problems/asteroid-collision/description/
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                top = stack.pop()
                if top == -asteroid:
                    break
                elif top > -asteroid:
                    stack.append(top)
                    break
            else:
                stack.append(asteroid)

        return stack
