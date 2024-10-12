# https://leetcode.com/problems/minimum-window-substring/description/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        t_map = {}
        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)

        window_map = {}
        have = 0
        need = len(t_map)
        result = [-1, -1]
        result_length = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_map[char] = 1 + window_map.get(char, 0)

            if char in t_map and window_map[char] == t_map[char]:
                have += 1

            while have == need:
                if right - left + 1 < result_length:
                    result = [left, right]
                    result_length = right - left + 1
                window_map[s[left]] -= 1
                if s[left] in t_map and window_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

        left, right = result
        return s[left : right + 1] if result_length != float("inf") else ""
