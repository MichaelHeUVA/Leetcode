# https://leetcode.com/problems/happy-number/description/


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        while n != 1:
            num = 0
            while n:
                num += pow(n % 10, 2)
                n = n // 10
            n = num
            if n in visited:
                return False
            visited.add(n)
        return True
