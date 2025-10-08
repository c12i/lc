class Solution(object):
    def maximumDifference(self, nums):
        min_num = float('inf')
        max_diff = -1

        for num in nums:
            min_num = min(min_num, num)
            diff = num - min_num
            max_diff = max(max_diff, diff)

        return max_diff if max_diff > 0 else -1
        