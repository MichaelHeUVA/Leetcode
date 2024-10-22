# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/


class Solution:
    def makeFancyString(self, s: str) -> str:
        output = []
        for char in s:
            if len(output) < 2 or (char != output[-1] or char != output[-2]):
                output.append(char)
        return "".join(output)
