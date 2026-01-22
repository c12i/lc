class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r = 0):
            if r == n:
                cp = ["".join(row) for row in board]
                res.append(cp)
                return
            
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack()

        return res