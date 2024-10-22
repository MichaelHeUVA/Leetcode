# https://leetcode.com/problems/merge-strings-alternately/description/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer_1 = 0
        pointer_2 = 0
        output = ""
        while pointer_1 < len(word1) and pointer_2 < len(word2):
            if (pointer_1 + pointer_2) % 2 == 0:
                output += word1[pointer_1]
                pointer_1 += 1
            else:
                output += word2[pointer_2]
                pointer_2 += 1

        if pointer_1 < len(word1):
            output += word1[pointer_1:]
        elif pointer_2 < len(word2):
            output += word2[pointer_2:]
        return output
