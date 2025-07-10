class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1

        while i > 0:
            if nums[i] == nums[i - 1]:
                del nums[i]
            i -= 1

        return len(nums)
