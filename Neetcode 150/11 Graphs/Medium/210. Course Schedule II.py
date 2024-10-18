# https://leetcode.com/problems/course-schedule-ii/description/
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])
        result = []
        visited = {}  # {number: "visited" "visiting"}

        def dfs(node):
            if node in visited:
                return visited[node] == "visited"

            visited[node] = "visiting"
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = "visited"
            result.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result
