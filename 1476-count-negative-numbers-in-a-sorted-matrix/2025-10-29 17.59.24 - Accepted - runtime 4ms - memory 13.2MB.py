class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] < 0:
                    count += 1
        return count
        