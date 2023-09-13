class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # get matrix length
        n = len(matrix)
        # loop through each layer inwards
        for layer in range(n // 2):
            # i represents the start index basis, we start at the current layer as the basis of the swap
            i = layer
            # end represents the end indexes' basis
            end = (n - 1) - layer
            while i < end:
                # get offset from outermost layer(s)
                offset = i - layer
                # keep ref to top left
                top_left = matrix[layer][i]
                # bottom left <- top left
                matrix[layer][i] = matrix[end - offset][layer]
                # bottom right <- bottom left
                matrix[end - offset][layer] = matrix[end][end - offset]
                # top right <- bottom right
                matrix[end][end - offset] = matrix[i][end]
                # top left <- top right
                matrix[i][end] = top_left
                # increment i
                i += 1

