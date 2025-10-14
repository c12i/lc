class Solution(object):
    def nextGreaterElement(self, n):
        nums = list(str(n))
        
        i, j = len(nums) - 1, len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            return -1  # No next greater
        
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1
        
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = reversed(nums[i:])
        
        result = int("".join(nums))
        return result if result <= 2**31 - 1 else -1