# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # sentence1 will always be shorter
        if len(sentence2) < len(sentence1):
            return self.areSentencesSimilar(sentence2, sentence1)
        s1 = sentence1.split()
        s2 = sentence2.split()
        prefix = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                prefix += 1
            else:
                break
        suffix = 0
        for i in range(len(s1)):
            if s1[len(s1) - 1 - i] == s2[len(s2) - 1 - i]:
                suffix += 1
            else:
                break
        return prefix + suffix >= len(s1)
