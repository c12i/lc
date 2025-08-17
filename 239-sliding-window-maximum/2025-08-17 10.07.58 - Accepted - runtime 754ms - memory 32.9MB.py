class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left = 0
        result = []
        
        max_heap = []

        for right, n in enumerate(nums):
            heapq.heappush(max_heap, (-n, right))

            if right - left + 1 == k:
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)

                result.append(-max_heap[0][0])
                left += 1

        return result

        