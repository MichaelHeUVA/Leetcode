# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = []
        for c in s:
            num.append(str(ord(c) - ord("a") + 1))
        num = "".join(num)
        for _ in range(k):
            num = sum(list(map(int, str(num))))
        return num
