class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)
            max_prod = max(max_prod, curr_max)

        return max_prod
