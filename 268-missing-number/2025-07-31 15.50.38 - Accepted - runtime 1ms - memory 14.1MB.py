class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for n in range(len(nums) + 1):
            if n not in nums:
                return n

        return -1