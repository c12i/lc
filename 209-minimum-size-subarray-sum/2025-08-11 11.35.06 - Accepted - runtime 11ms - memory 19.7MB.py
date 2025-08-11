class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window_sum = 0
        res = float('inf')

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if res == float('inf') else res
                