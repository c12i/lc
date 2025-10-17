class Solution(object):
    def spiralOrder(self, matrix):
        M, N = len(matrix), len(matrix[0])  # M = rows, N = cols
        TOTAL = M * N

        left_col, right_col = 0, N - 1 
        top_row, bottom_row = 0, M - 1     

        elts = []

        while len(elts) < TOTAL:
            # Move right along top row
            for col in range(left_col, right_col + 1):
                #  check handles non-square matrices where you might finish collecting all elements in the middle of a directional move.
                if len(elts) < TOTAL:
                    elts.append(matrix[top_row][col])
            top_row += 1

            # Move down along right column
            for row in range(top_row, bottom_row + 1):
                if len(elts) < TOTAL:
                    elts.append(matrix[row][right_col])
            right_col -= 1

            # Move left along bottom row
            for col in range(right_col, left_col - 1, -1):
                if len(elts) < TOTAL:
                    elts.append(matrix[bottom_row][col])
            bottom_row -= 1

            # Move up along left column
            for row in range(bottom_row, top_row - 1, -1):
                if len(elts) < TOTAL:
                    elts.append(matrix[row][left_col])
            left_col += 1

        return elts