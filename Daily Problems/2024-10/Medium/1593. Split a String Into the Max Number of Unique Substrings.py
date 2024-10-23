# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/?envType=daily-question&envId=2024-10-21


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        max_length = 0

        def backtrack(index, path):
            nonlocal max_length
            if index == n:
                max_length = max(max_length, len(path))

            for i in range(index, n):
                if s[index : i + 1] not in path:
                    path.add(s[index : i + 1])
                    backtrack(i + 1, path)
                    path.remove(s[index : i + 1])

        backtrack(0, set())
        return max_length
