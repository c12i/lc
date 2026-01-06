class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        min_heap = []

        # Initialize heap with first element in nums2 paired with first k elements in nums1
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while min_heap and len(res) < k:
            total, i, j = heapq.heappop(min_heap)
            res.append((nums1[i], nums2[j]))

            # If possible, push next element in nums2 with same nums1[i]
            if j < len(nums2) - 1:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res