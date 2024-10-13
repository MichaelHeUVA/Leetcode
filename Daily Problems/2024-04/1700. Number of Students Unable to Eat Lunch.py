# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=daily-question&envId=2024-04-08
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        x = students.count(0)
        y = students.count(1)
        stack = sandwiches[::-1]
        while stack:
            if stack[-1] == 0:
                if x > 0:
                    x -= 1
                else:
                    return len(stack)
            else:
                if y > 0:
                    y -= 1
                else:
                    return len(stack)
            stack.pop()
        return 0
