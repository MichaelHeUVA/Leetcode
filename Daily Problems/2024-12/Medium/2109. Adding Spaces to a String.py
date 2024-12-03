# https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=daily-question&envId=2024-12-03
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)
        i = 0
        j = 0
        output = []
        while i < len(s):
            if j < len(spaces) and spaces[j] == i:
                output.append(" ")
                output.append(s[i])
                i += 1
                j += 1
            else:
                output.append(s[i])
                i += 1

        return "".join(output)
