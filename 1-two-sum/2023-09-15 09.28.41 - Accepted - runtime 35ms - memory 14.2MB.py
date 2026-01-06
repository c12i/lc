class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                sum_idx = hm[nums[i]]
                return [i, sum_idx]
            else:
                hm[target - nums[i]] = i
