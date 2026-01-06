class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
        # prefix_sum = 0
        # min_prefix = 0
        # max_sum = float('-inf')

        # for i in range(len(nums)):
        #     prefix_sum += nums[i]
        #     max_sum = max(max_sum, prefix_sum - min_prefix)
        #     min_prefix = min(min_prefix, prefix_sum)

        # return max_sum