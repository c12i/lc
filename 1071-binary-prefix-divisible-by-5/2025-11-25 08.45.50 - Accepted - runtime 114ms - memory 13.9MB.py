class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        decimal = 0
        res = []

        # O(N)
        for bit in nums:
            decimal = (decimal << 1) | bit
            res.append(decimal % 5 == 0)

        return res
