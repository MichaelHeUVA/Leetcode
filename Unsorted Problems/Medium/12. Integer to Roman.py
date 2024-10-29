# https://leetcode.com/problems/integer-to-roman/description/


class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        output = []
        for value, symbol in int_to_roman.items():
            if num == 0:
                break
            count, num = divmod(num, value)
            output.append(symbol * count)
        return "".join(output)
