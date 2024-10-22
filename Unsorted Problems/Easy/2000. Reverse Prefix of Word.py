# https://leetcode.com/problems/reverse-prefix-of-word/description/


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        output = []
        for i, c in enumerate(word):
            if ch == c:
                for j in range(i, -1, -1):
                    output.append(word[j])
                output.append(word[i + 1 : :])
                break

        return "".join(output) if output else word
