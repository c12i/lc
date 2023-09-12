class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_has_zeros = False
        col_has_zeros = False

        R = len(matrix)
        C = len(matrix[0])

        # loop through first row
        for i in range(C):
            if matrix[0][i] == 0:
                row_has_zeros = True
                break

        # loop through matrix's first columns
        for i in range(R):
            if matrix[i][0] == 0:
                col_has_zeros = True
                break

        
        # look for zeros in the rest of the matrix, update both the first row and col
        for r in range(1, R):
            for c in range(1, C):
                 if matrix[r][c] == 0:
                     matrix[0][c] = 0
                     matrix[r][0] = 0

        # nullify cols based on first row
        for i in range(1, C):
            if matrix[0][i] == 0:
                for r in range(1, R):
                    matrix[r][i] = 0

        # nullify rows base on first col
        for i in range(1, R):
            if matrix[i][0] == 0:
                for c in range(1, C):
                    matrix[i][c] = 0

        # nullify first row if first row had zeros
        if row_has_zeros:
            for c in range(C):
                matrix[0][c] = 0

        # nullify first col if first col had zeros
        if col_has_zeros:
            for r in range(R):
                matrix[r][0] = 0
