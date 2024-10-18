# https://leetcode.com/problems/course-schedule/description/
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        visited = [
            0
        ] * numCourses  # 0 means not visited 1 means visiting 2 means visited

        def dfs(node):
            if visited[node] == 2:
                return True
            if visited[node] == 1:
                return False
            visited[node] = 1
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
