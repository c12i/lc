class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [n for n in nums if n % 6 == 0]
        n = len(nums)
        return sum(nums) // n if n > 0 else 0