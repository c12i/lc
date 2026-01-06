"""
what I can do, get all permutations of nums -> get + 1 of nums
"""
class Solution(object):
    def nextPermutation(self, nums):
        i, j = len(nums) - 1, len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = reversed(nums[i:])
