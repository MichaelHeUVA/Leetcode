# https://leetcode.com/problems/n-queens-ii/description/


class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        row_set = set()
        diag_set = set()
        anti_diag_set = set()
        self.output = 0

        def backtrack(row):
            if row == n:
                self.output += 1
                return

            for col in range(n):
                if (
                    col in col_set
                    or row in row_set
                    or (row - col) in diag_set
                    or (row + col) in anti_diag_set
                ):
                    continue
                col_set.add(col)
                row_set.add(row)
                diag_set.add((row - col))
                anti_diag_set.add((row + col))

                backtrack(row + 1)

                col_set.remove(col)
                row_set.remove(row)
                diag_set.remove((row - col))
                anti_diag_set.remove((row + col))

        backtrack(0)
        return self.output
