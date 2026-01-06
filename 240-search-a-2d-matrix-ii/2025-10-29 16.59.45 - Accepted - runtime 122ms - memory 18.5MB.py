class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            curr = matrix[row][col]

            if curr == target:
                return True
            if curr > target:
                col -= 1
            else:
                row += 1

        return False
