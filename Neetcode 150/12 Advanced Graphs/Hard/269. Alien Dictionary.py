# https://leetcode.com/problems/alien-dictionary/description/
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build adjacency list
        adj_list = {character: set() for word in words for character in word}
        # put pairs of characters into the adj_list
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLength = min(len(word1), len(word2))
            # if the word1 is longer and the prefix is the same this is invalid
            # Example: [apple, app] this is invalid
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            # find the first difference in characters between the two words
            for j in range(minLength):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].add(word2[j])
                    break

        visited = {}  # {character : "visited" or "current_path"}
        result = []

        # post order dfs / topological sort
        def dfs(node):
            if node in visited:
                return visited[node] == "current_path"

            visited[node] = "current_path"

            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True

            visited[node] = "visited"
            result.append(node)

        for node in adj_list:
            if dfs(node):
                return ""

        # since it's post order reverse the list
        result.reverse()

        return "".join(result)
