import heapq

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        arr = [(-x, i) for i, x in enumerate(nums)]
        heapq.heapify(arr)

        result = []

        for _ in range(k):
            num, idx = heapq.heappop(arr)
            result.append((-num, idx))
        
        result.sort(key = lambda i : i[1])

        return [n for n, _ in result]
        