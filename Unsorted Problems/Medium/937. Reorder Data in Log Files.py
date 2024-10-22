# https://leetcode.com/problems/reorder-data-in-log-files/description/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        queue = []
        ans = []
        for i in logs:
            if i.split()[1].isnumeric():
                queue.append(i)
            else:
                ans.append(i)
        ans.sort(key=lambda x: x.split()[0])
        ans.sort(key=lambda x: x.split()[1:])
        return ans + queue
