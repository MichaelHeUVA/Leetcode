# https://leetcode.com/problems/simplify-path/description/


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for directory in path:
            if not directory or directory == ".":
                continue
            if directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        return "/" + "/".join(stack)
