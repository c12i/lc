class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        farthest = 0
        i = 0

        while i <= farthest:
            farthest = max(farthest, i + nums[i])

            if farthest >= n - 1:  
                return True
            i += 1 

        return False
