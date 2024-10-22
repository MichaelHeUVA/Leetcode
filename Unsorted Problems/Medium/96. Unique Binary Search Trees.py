# https://leetcode.com/problems/unique-binary-search-trees/description/
from math import comb


class Solution:
    def numTrees(self, n: int) -> int:
        return comb(2 * n, n) // (n + 1)
