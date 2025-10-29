class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def checkIncreasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for i in range(len(nums) - 2 * k + 1):
            if checkIncreasing(i) and checkIncreasing(i + k):
                return True
        return False