class Solution(object):
    def generateMatrix(self, n):
        N = n * n
        
        top_row, bottom_row = 0, n - 1
        left_col, right_col = 0, n - 1

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        s = 1 
        while s <= N:
            for col in range(left_col, right_col + 1):
                matrix[top_row][col] = s
                s += 1
            top_row += 1

            for row in range(top_row, bottom_row + 1):
                matrix[row][right_col] = s
                s += 1
            right_col -= 1

            for col in range(right_col, left_col - 1, -1):
                matrix[bottom_row][col] = s
                s += 1
            bottom_row -= 1

            for row in range(bottom_row, top_row - 1, -1):
                matrix[row][left_col] = s
                s += 1
            left_col += 1

        return matrix