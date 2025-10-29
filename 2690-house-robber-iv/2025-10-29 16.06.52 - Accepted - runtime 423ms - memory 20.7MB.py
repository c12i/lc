class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def good(target):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= target:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        low, high = min(nums), max(nums)

        while low < high:
            mid = (low + high) // 2

            if good(mid):
                high = mid 
            else:
                low = mid + 1

        return low