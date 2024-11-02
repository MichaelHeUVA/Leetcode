# https://leetcode.com/problems/count-and-say/description/


class Solution:
    def countAndSay(self, n: int) -> str:
        output = ["1"]

        def count_entries():
            nonlocal output
            prev = output[0]
            new_output = []
            count = 1
            for i in range(1, len(output)):
                if prev == output[i]:
                    count += 1
                else:
                    new_output.append(str(count))
                    new_output.append(prev)
                    prev = output[i]
                    count = 1
            new_output.append(str(count))
            new_output.append(prev)
            output = new_output

        for i in range(n - 1):
            count_entries()

        return "".join(output)
