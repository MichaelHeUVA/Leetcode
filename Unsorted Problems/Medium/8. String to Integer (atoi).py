# https://leetcode.com/problems/string-to-integer-atoi/description/


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = False
        output = 0
        for i, char in enumerate(s):
            if i == 0 and char == "-":
                negative = True
            elif char.isnumeric():
                output *= 10
                output += int(char)
            elif not (i == 0 and char == "+"):
                break
        if negative and output > 2_147_483_648:
            output = 2_147_483_648
        elif not negative and output > 2_147_483_647:
            output = 2_147_483_647
        return -output if negative else output
