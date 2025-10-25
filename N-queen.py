class Solution:
    def solveNQueen(self, n: int) -> list[list[str]]:
        cols = set()
        negDiag = set()  # (r - c)
        posDiag = set()  # (r + c)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtracking(r):
            if r == n:  # placed queens in all rows
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r - c) in negDiag or (r + c) in posDiag:
                    continue

                # place queen
                cols.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = "Q"

                # go to next row
                backtracking(r + 1)

                # remove queen (backtrack)
                cols.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = "."

        backtracking(0)
        return res


# Example run
n = 4
solution = Solution()
output = solution.solveNQueen(n)
for sol in output:
    for row in sol:
        print(row)
    print()
