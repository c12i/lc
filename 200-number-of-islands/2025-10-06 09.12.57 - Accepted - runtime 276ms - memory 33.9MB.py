"""
Iterate through the grid, for every "1" we encoutner, increment the island count and perform DFS
visiting all other adjacent "1"s exhaustively
"""

class Solution(object):
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                (r < 0 or c < 0) or
                (r >= ROWS or c >= COLS) or
                ((r, c) in visited) or
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc)

        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands