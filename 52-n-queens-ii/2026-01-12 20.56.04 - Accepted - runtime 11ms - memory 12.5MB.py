class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = set()
        pos_diag = set()
        neg_diag = set()
        self.res = 0
        board = [["."] * n for _ in range(n)]

        def backtrack(r = 0):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if c in col or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue

                col.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                board[r][c] = "."

        backtrack()

        return self.res