DIRECTIONS = [
    (-1, 0), # up
    (1, 0), # down
    (0, -1), # left
    (0, 1) # right
]

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, self.dfs(grid, r, c, visited))

        return max_area
        

    def dfs(self, grid, row, col, visited):
        if (
            (row < 0 or col < 0) or
            (row >= len(grid) or col >= len(grid[0])) or
            ((row, col) in visited) or
            grid[row][col] == 0
        ):
            return 0

        visited.add((row, col))
        area = 1

        for dr, dc in DIRECTIONS:
            area += self.dfs(grid, row + dr, col + dc, visited)

        return area

       