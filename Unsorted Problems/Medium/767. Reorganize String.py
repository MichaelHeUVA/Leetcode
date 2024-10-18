# https://leetcode.com/problems/reorganize-string/description/
from collections import Counter
from heapq import heappop, heappush


# Priority Queue
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        pq = []
        for key, val in counts.items():
            heappush(pq, (-val, key))
        output = []

        while pq:
            count, char = heappop(pq)
            count = -count
            if output and output[-1] == char:
                if not pq:
                    return ""
                count2, char2 = heappop(pq)
                count2 = -count2
                output.append(char2)
                count2 -= 1
                if count2:
                    heappush(pq, (-count2, char2))
                heappush(pq, (-count, char))
            else:
                output.append(char)
                count -= 1
                if count:
                    heappush(pq, (-count, char))

        return "".join(output)


# Counting and odd even
class Solution:  # noqa F811
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        max_count = 0
        max_char = ""
        for char, count in counts.items():
            if count > max_count:
                max_count = count
                max_char = char
        if max_count > (n + 1) // 2:
            return ""

        output = [""] * n
        index = 0

        while counts[max_char] != 0:
            output[index] = max_char
            index += 2
            counts[max_char] -= 1

        for char, count in counts.items():
            while count > 0:
                if index >= n:
                    index = 1
                output[index] = char
                index += 2
                count -= 1

        return "".join(output)
