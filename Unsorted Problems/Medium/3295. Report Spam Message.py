# https://leetcode.com/problems/report-spam-message/description/
from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        count = 0
        for word in message:
            if word in banned:
                count += 1
        return count >= 2
