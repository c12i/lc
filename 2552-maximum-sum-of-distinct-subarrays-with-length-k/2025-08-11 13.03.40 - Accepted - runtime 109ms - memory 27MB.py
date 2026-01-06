class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        left = 0
        window_sum = 0
        max_sum = float('-inf')
        seen = set()

        for right, x in enumerate(nums):
            while x in seen:
                y = nums[left]
                seen.remove(y)
                window_sum -= y
                left += 1
                
            seen.add(x)
            window_sum += x

            if right - left + 1 == k:
                if window_sum > max_sum:
                    max_sum = window_sum
                y = nums[left]
                seen.remove(y)
                window_sum -= y
                left += 1

        return 0 if max_sum == float('-inf') else max_sum