# https://leetcode.com/problems/longest-happy-string/description/?envType=daily-question&envId=2024-10-16
from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        output = []
        if a:
            heappush(max_heap, (-a, "a"))
        if b:
            heappush(max_heap, (-b, "b"))
        if c:
            heappush(max_heap, (-c, "c"))
        while max_heap:
            count, char = heappop(max_heap)
            count = -count

            if len(output) >= 2 and output[-1] == char and output[-2] == char:
                if not max_heap:
                    break
                second_count, second_char = heappop(max_heap)
                second_count += 1
                output.append(second_char)
                if second_count:
                    heappush(max_heap, (second_count, second_char))
                heappush(max_heap, (-count, char))
            else:
                count -= 1
                output.append(char)
                if count:
                    heappush(max_heap, (-count, char))

        return "".join(output)
