class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def is_feasible(s):
            count = 1
            rem = s
            for i in range(len(nums)):
                if rem >= nums[i]:
                    rem -= nums[i]
                else:
                    count += 1
                    rem = s - nums[i]
            return count <= k

        low, high = max(nums), sum(nums)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
            