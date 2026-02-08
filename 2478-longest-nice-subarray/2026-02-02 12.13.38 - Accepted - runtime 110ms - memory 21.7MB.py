class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        left = 0
        max_len = 0
        niceness = 0

        for right in range(n):
            while niceness & nums[right] != 0:
                niceness ^= nums[left]
                left += 1

            niceness |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len