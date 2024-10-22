# https://leetcode.com/problems/word-pattern/description/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_to_word = {}
        word_to_letter = {}
        string_array = s.split()
        if len(pattern) != len(string_array):
            return False
        for i, letter in enumerate(pattern):
            if letter not in letter_to_word:
                letter_to_word[letter] = string_array[i]
            if string_array[i] not in word_to_letter:
                word_to_letter[string_array[i]] = letter
            if (
                letter_to_word[letter] != string_array[i]
                or word_to_letter[string_array[i]] != letter
            ):
                return False
        return True
