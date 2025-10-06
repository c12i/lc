"""
Values to keep track of:
- visited coordniates
- count of battleships

Scan through every cell in the grid. If "X". Perform DFS to identify the rest of the battleship
"""
class Solution(object):
    def countBattleships(self, board):
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if (
                (r < 0 or c < 0) or
                (r >= ROWS or c >= COLS) or
                (r, c) in visited or
                board[r][c] != "X"
            ):
                return
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc)
            

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)

        return count
