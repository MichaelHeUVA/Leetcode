# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/?envType=daily-question&envId=2024-12-04


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        pointer = 0
        for i in range(len(str1)):
            if pointer >= len(str2):
                return True
            if (
                str1[i] == str2[pointer]
                or chr((ord(str1[i]) - ord("a") + 1) % 26 + ord("a")) == str2[pointer]
            ):
                pointer += 1

        return pointer == len(str2)
