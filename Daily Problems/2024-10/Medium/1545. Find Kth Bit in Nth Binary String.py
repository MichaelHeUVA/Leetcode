# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2024-10-19


# Optimized
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert_count = 0
        length = 2**n - 1

        while k > 1:
            if k == length // 2 + 1:
                return "1" if invert_count % 2 == 0 else "0"

            if k > length // 2:
                k = length + 1 - k
                invert_count += 1

            length //= 2

        return "1" if invert_count % 2 else "0"


# Brute force
class Solution:  # noqa F811
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n):
            s_reverse_invert = []
            for j in reversed(range(len(s))):
                if s[j] == "0":
                    s_reverse_invert.append("1")
                else:
                    s_reverse_invert.append("0")
            s_reverse_invert = "".join(s_reverse_invert)
            s = s + "1" + s_reverse_invert
        return str(s[k - 1])
