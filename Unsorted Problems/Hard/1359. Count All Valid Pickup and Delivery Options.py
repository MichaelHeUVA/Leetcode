# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
from math import factorial


class Solution:
    def countOrders(self, n: int) -> int:
        mod = int(1e9 + 7)
        return factorial(2 * n) // 2**n % mod
