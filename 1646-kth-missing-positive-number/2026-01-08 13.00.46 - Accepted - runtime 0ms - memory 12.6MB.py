class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        s = set(arr)
        count = 0

        for n in range(1, max(arr) + k + 1):
            if n not in s:
                count += 1
                if count == k:
                    return n