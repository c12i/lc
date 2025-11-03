class Solution(object):
    def findMiddleIndex(self, nums):
        prefix_sum = 0
        total = sum(nums)

        for i, n in enumerate(nums):
            if prefix_sum == total - (prefix_sum + n):
                return i
            prefix_sum += n
        return -1