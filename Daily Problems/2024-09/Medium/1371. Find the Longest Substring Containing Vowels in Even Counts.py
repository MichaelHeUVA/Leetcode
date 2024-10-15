# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/?envType=daily-question&envId=2024-09-15


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        character_map = [0] * 26
        character_map[ord("a") - ord("a")] = 1
        character_map[ord("e") - ord("a")] = 2
        character_map[ord("i") - ord("a")] = 4
        character_map[ord("o") - ord("a")] = 8
        character_map[ord("u") - ord("a")] = 16
        prefix_xor = 0
        longest_substring = 0
        prefix_map = [-1] * 32  # 0 - 31 where 31 is all vowels xored together
        for i in range(len(s)):
            prefix_xor ^= character_map[ord(s[i]) - ord("a")]

            if prefix_map[prefix_xor] == -1 and prefix_xor != 0:
                prefix_map[prefix_xor] = i
            longest_substring = max(longest_substring, i - prefix_map[prefix_xor])

        return longest_substring
