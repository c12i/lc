class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) 

        for layer in range(n // 2):
            last = (n - 1) - layer
            i = layer
            while i < last:
                offset = i - layer 
                top = matrix[layer][i] 
                # left -> top
                matrix[layer][i] = matrix[last - offset][layer]
                # bottom -> left
                matrix[last - offset][layer] = matrix[last][last - offset]
                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]
                # top -> right
                matrix[i][last] = top # right <- saved top
                i += 1
                