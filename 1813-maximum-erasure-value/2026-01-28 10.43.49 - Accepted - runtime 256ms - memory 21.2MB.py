class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = set()
        running_sum = 0
        max_score = float('-inf')
        left = 0

        for right in range(len(nums)):
            running_sum += nums[right]

            while nums[right] in uniq:
                uniq.remove(nums[left])
                running_sum -= nums[left]
                left += 1

            uniq.add(nums[right])
            max_score = max(max_score, running_sum)

        return max_score