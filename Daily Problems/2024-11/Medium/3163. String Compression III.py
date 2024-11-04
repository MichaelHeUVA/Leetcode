# https://leetcode.com/problems/string-compression-iii/description/?envType=daily-question&envId=2024-11-04


class Solution:
    def compressedString(self, word: str) -> str:
        prev = word[0]
        count = 0
        output = []
        for char in word:
            if char == prev:
                count += 1
                if count == 9:
                    output.append(str(count))
                    output.append(prev)
                    count = 0
            elif count > 0:
                output.append(str(count))
                output.append(prev)
                prev = char
                count = 1
            else:
                prev = char
                count = 1
        if count > 0:
            output.append(str(count))
            output.append(prev)

        return "".join(output)
