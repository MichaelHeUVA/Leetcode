# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(index, combination):
            if len(combination) == len(digits):
                result.append(combination)
                return

            for letter in map[digits[index]]:
                backtrack(index + 1, combination + letter)
            return

        if digits:
            backtrack(0, "")

        return result
