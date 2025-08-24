class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        maxLength = float('-inf')
        zeroIdx = None


        for right, num in enumerate(nums):
            if nums[right] == 0:
                if zeroIdx is not None:
                    left = zeroIdx + 1
                zeroIdx = right
            maxLength = max(maxLength, right - left)

        return maxLength

        