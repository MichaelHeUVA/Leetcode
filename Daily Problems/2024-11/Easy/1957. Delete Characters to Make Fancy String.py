# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2024-11-01


class Solution:
    def makeFancyString(self, s: str) -> str:
        output = []
        for char in s:
            if len(output) < 2 or (char != output[-1] or char != output[-2]):
                output.append(char)
        return "".join(output)
