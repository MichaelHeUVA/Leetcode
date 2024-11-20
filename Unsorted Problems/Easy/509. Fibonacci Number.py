# https://leetcode.com/problems/fibonacci-number/description/

# Formula
class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + (5**0.5)) / 2
        return int(round((golden_ratio**n) / (5**0.5)))


# Recursive
class Solution:  # noqa F811
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
