class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        prod = 1
        ans = 0
        l = 0

        for r in range(len(nums)):
            prod *= nums[r]

            while prod >= k:
                prod //= nums[l]
                l += 1

            ans += (r - l) + 1

        return ans