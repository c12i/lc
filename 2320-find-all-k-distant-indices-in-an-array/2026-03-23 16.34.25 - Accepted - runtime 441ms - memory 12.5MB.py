class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        indices = [i for i in range(n) if nums[i] == key]
        seen = set()
        res = []

        for i in indices:
            for j in range(n):
                if abs(i - j) <= k:
                    if j not in seen:
                        res.append(j)
                        seen.add(j)


        return res
        