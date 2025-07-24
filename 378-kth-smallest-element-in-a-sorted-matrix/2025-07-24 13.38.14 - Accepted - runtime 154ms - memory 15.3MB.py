import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        flattened = []

        for i in range(n):
            for j in range(n):
                heapq.heappush(flattened, matrix[i][j])

        for i in range(k - 1):
            val = heapq.heappop(flattened)

        result = heapq.heappop(flattened)

        return result