class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def checkMagicSquare(r, c):
            end_row = r + 2
            end_col = c + 2

            
            row_sums = set()
            col_sums = set()
            diagonal_sums = set()
            nums = set()

            row = r
            while row <= end_row:
                s = 0
                for col in range(c, end_col + 1):
                    s += grid[row][col]
                    if grid[row][col] <= 9 and grid[row][col] >= 1: nums.add(grid[row][col])
                row_sums.add(s)
                row += 1

            if len(nums) != 9:
                return False

            col = c
            while col <= end_col:
                s = 0
                for row in range(r, end_row + 1):
                    s += grid[row][col]
                col_sums.add(s)
                col += 1
            
            diagonal_sums.add(
                grid[r][c] + grid[r + 1][c + 1] + grid[end_row][end_col]
            )
            diagonal_sums.add(
                grid[end_row][c] + grid[end_row - 1][c + 1] + grid[end_row - 2][end_col]
            )

            if len(row_sums) == 1 and len(col_sums) == 1 and len(diagonal_sums) == 1:
                return list(row_sums)[0] == list(col_sums)[0] == list(diagonal_sums)[0]

            return False
                
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if r + 2 >= rows or c + 2 >= cols:
                    continue
                if checkMagicSquare(r, c):
                    ans += 1

        return ans
                