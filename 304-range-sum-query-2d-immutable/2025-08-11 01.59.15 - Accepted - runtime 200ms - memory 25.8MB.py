class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.P = [[0]]
            return

        m, n = len(matrix), len(matrix[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.P[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.P[i - 1][j]
                    + self.P[i][j - 1]
                    - self.P[i - 1][j - 1]
                )
        self.matrix = matrix

    

    def sumRegion(self, row1, col1, row2, col2):
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.P[r2][c2]
            - self.P[r1 - 1][c2]
            - self.P[r2][c1 - 1]
            + self.P[r1 - 1][c1 - 1]
        )
        

    # brute force
    # def sumRegion(self, row1, col1, row2, col2):
    #     """
    #     :type row1: int
    #     :type col1: int
    #     :type row2: int
    #     :type col2: int
    #     :rtype: int
    #     """
    #     s = 0

    #     while row1 <= row2:
    #         for i in range(col1, col2 + 1):
    #             s += self.matrix[row1][i]
    #         row1 += 1

    #     return s

            

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)