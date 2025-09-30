class Solution(object):
    def minOperations(self, nums, x):
        """
        Instead of tracking the ends we remove, we can flip the problem:
Find the longest contiguous subarray in nums with sum = target.
        """
        total = sum(nums)
        target = total - x

        left = 0
        prefix_sum = 0
        max_len = float('-inf')

        for right in range(len(nums)):
            prefix_sum += nums[right]

            while prefix_sum > target and left <= right:
                prefix_sum -= nums[left]
                left += 1

            if prefix_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == float('-inf') else len(nums) - max_len