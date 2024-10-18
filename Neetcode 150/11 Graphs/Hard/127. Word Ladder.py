# https://leetcode.com/problems/word-ladder/description/
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q = deque([beginWord])
        distance = 1

        while q:
            size = len(q)
            distance += 1
            for _ in range(size):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        temp = word[:i] + chr(ord("a") + j) + word[i + 1 :]

                        if temp == endWord:
                            return distance

                        if temp in word_set:
                            q.append(temp)
                            word_set.remove(temp)

        return 0
