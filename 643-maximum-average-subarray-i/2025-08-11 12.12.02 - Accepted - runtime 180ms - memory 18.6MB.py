class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        window_sum = 0
        max_av = float('-inf')

        for right, num in enumerate(nums):
            window_sum += num

            if right - left + 1 == k:
                max_av = max(max_av, float(window_sum) / k)
                window_sum -= nums[left]
                left += 1

        return max_av